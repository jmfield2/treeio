
from treeio.messaging.models import Message, MessageStream
from treeio.identities.models import Contact, ContactType

from django.db.models import Q

import email
import sifter.parser
import datetime

class Command(object):

	def __init__(self):

		return

		f=open("test.sieve", "U")
		rules = sifter.parser.parse_file(f)

		msgs = Message.objects.all() #Q(stream=)
		for m in msgs:
			rfc=unicode(m.rfc822).encode('utf-8', errors='replace')

			e = email.message_from_string(rfc)
			ret=rules.evaluate(e)
			if len(ret) > 0 and ret[0][0] == "fileinto": 
				s = MessageStream.objects.filter(Q(name=ret[0][1][0]))
				if s.count() == 1:
					stream = s.all()[0]
					if m.stream <> stream:
						m.stream = stream
						m.save()
					print ret[0][1]
					print m.title


        def run_from_argv(self, *args, **options):

		from clint.textui import progress
		from time import sleep
	
		#for i in progress.bar(range(100), label="test: "):

		streams = MessageStream.objects.filter(trash=False, incoming_server_username__isnull=False)

		for s in streams:
		        print "%s=%d" % (s.name, Message.objects.filter(Q(stream=s)).count())
			# XXX IMAP 
		        s.process_email()


	
