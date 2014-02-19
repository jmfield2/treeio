# encoding: utf-8
# Copyright 2011 Tree.io Limited
# This file is part of Treeio.
# License www.tree.io/license

"""
Messaging Emails
"""

from threading import Thread
from django.db.models import Q
from django.utils.html import strip_tags
from treeio.core.models import ModuleSetting
from treeio.core.mail import BaseEmail, SystemEmail
from treeio.identities.models import Contact, ContactType

from treeio.core.mail import EmailReceiver

class EmailStream(EmailReceiver):
    "EmailStream"
    active = False
    
    def __init__(self, stream):
        self.stream = stream
        self.active = True
        try:
            conf = ModuleSetting.get_for_module('treeio.messaging', 'default_imap_folder')[0]
            folder_name = conf.value
        except:
            folder_name = None
        super(EmailStream, self).__init__(stream.incoming_server_type, stream.incoming_server_name,
                                          stream.incoming_server_username, stream.incoming_password, folder_name)
        
    def process_msg(self, msg, attrs, attachments):
        "Save message, Cap!"
        from treeio.messaging.models import Message

        try:
            conf = ModuleSetting.get_for_module('treeio.messaging', 'default_contact_type')[0]
            default_contact_type = ContactType.objects.get(pk=long(conf.value))
        except:
            default_contact_type = None

        email_author, created = Contact.get_or_create_by_email(attrs.author_email, attrs.author_name, default_contact_type)
        if created:
            email_author.copy_permissions(self.stream)

        # check if the message is already retrieved

	# XXX body=attrs.body removed, should store a unique 'msg-id'
        existing = Message.objects.filter(stream=self.stream, title=attrs.subject, author=email_author).exists()
        if not existing:
            message = None
            if attrs.subject[:3] == 'Re:':
                # process replies
                if attrs.subject[:4] == 'Re: ':
                    original_subject = attrs.subject[4:]
                else:
                    original_subject = attrs.subject[3:]

                try:
                    query = Q(reply_to__isnull=True) & Q(recipients=email_author) & (Q(title=original_subject) | Q(title=attrs.subject))
                    original = Message.objects.filter(query).order_by('-date_created')[:1][0]
                    message = Message(title=attrs.subject, body=str(attrs.body).decode('unicode_escape', errors='replace'), author=email_author,
                                    stream=self.stream, reply_to=original)
                    if attrs.email_date:
                        message.date_created = attrs.email_date

		    message.rfc822 = msg.as_string().decode('unicode_escape', errors='replace')

                    message.save()
                    message.copy_permissions(original)
                    original.read_by.clear()
                except IndexError:
                    pass
            if not message:
                message = Message(title=attrs.subject, body=str(attrs.body).decode('unicode_escape', errors='replace'), author=email_author, stream=self.stream)
                if attrs.email_date:
                    message.date_created = attrs.email_date

		message.rfc822 = msg.as_string().decode('unicode_escape', errors='replace') #utf-8', errors='replace')

                message.save()
                message.copy_permissions(self.stream)
                message.recipients.add(email_author)
        
class EmailMessage(Thread):
    "Email Message"

    def __init__(self, message):
        Thread.__init__(self)
        self.message = message
        
    def run(self):
        "Run"
        self.process_email()
        
    def send_email(self):
        "Send email"
        self.process_email()
        
    def get_smtp_port(self):
        "Returns tuple (port, ssl) for current message's stream"
        
        port = 25
        ssl = False
        
        if self.message.stream.outgoing_server_type == "SMTP-SSL":
            ssl = True
        
        return port, ssl
        
        
    def process_email(self):  
        "Process email"
        message = self.message
        if message.reply_to:
            subject = "Re: %s" % message.reply_to.title
        else:
            subject = message.title
        body = strip_tags(message.body)
        html = message.body
        
        for recipient in message.recipients.all():
            if recipient.id == message.author_id:
                # don't send email to message author
                continue
            
            toaddr = recipient.get_email()
            
            if message.stream and message.stream.outgoing_server_name:
                fromaddr = unicode(message.author) + ' <' + unicode(message.stream.outgoing_email) + '>'
                login = message.stream.outgoing_server_username
                password = message.stream.outgoing_password
                
                port, ssl = self.get_smtp_port()
               
		if ":" in message.stream.outgoing_server_name:
			tmp = message.stream.outgoing_server_name.split(':')
			port = int(tmp[1])
			message.stream.outgoing_server_name = tmp[0]
 
                BaseEmail(message.stream.outgoing_server_name, 
                    login, password, fromaddr, toaddr, subject,
                    body, signature=None, html=html, port=port, ssl=ssl).send_email()
            
            else:
                SystemEmail(toaddr, subject, body, signature=None, html=html).send_email()
