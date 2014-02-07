
from treeio.messaging.models import Message, MessageStream
from treeio.identities.models import Contact, ContactType

from django.db.models import Q

import email
import sifter.parser

class Command(object):

	def __init__(self):
		print "hello"

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

		stream = args[0][2] if len(args[0]) > 2 else ""
		sieve = args[0][3] if len(args[0]) > 3 else "test.sieve"

                f=open(sieve, "U")
                rules = sifter.parser.parse_file(f)

		if len(stream) > 0:
			original = MessageStream.objects.filter(Q(name=stream)).all()[0]
			msgs = Message.objects.filter(Q(stream=original))
		else:
	                msgs = Message.objects.all() #Q(stream=)

                for m in msgs:
                        rfc=unicode(m.rfc822).encode('utf-8', errors='replace')

			# XXX seperate body comparisons
			if "http://" in m.body:
				m.delete()

		'''
		c = Contact.objects.filter(Q(id=109)).all()[0]
		c.contact_type = ContactType.objects.get(Q(name='Person'))
	        c.save()
		'''


	
