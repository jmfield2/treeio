
from treeio.messaging.models import Message, MessageStream
from treeio.identities.models import Contact, ContactType

from django.db.models import Q

import email
import sifter.parser

import datetime

class Command(object):

	def __init__(self):
		print "hello"

        def run_from_argv(self, *args, **options):

		import finance.models as finance
		import core.models as models
		from collections import OrderedDict
		import csv, math

		uncat = finance.Category.objects.filter(Q(name__startswith="Uncat")).all()[0]

		f = finance.Transaction.objects.filter(Q(category=uncat)).all()
		print len(f)
		
		file = "cats.txt"
		#me = Contact.objects.filter(Q(name='Total Travel Marketing, Inc.')).all()[0]
		me = Contact.objects.filter(Q(name="Joseph Fields")).all()[0]

		with open(file, "rb") as csvfile:
			reader = csv.reader(csvfile, delimiter='|', quotechar='"')
			for line in reader:

				f = finance.Transaction.objects.filter(Q(category=uncat) & Q(name__icontains=line[0]) ).all()
				print "%s == %d" % (line, len(f))

				for row in f:
					row.category = finance.Category.objects.filter(Q(name=line[1])).all()[0]
					row.save()

		return;

		from django.core.cache import cache
		import time

		cache.set('hardtree_default_last', time.time() - 100)

		print cache.get('treeio_default_multi') #:1:jc_treeio_default_multi_00e9aaec619ac71d4a2c7647efb5395a')
		print cache.get('hardtree_default_last')
		return

		from treeio.projects.models import Project

		p = Project.objects.all()
		print p
		print Project.objects.filter().query

		return

		import core.models as models
		
		mod = models.Module.objects.get(name='treeio.messaging')

		a = mod.full_access.filter().query
		print a

		u = models.User.objects.filter(Q(name='Admin'))
		print u.all()[0]
		print u.query
		return

		print models.Object.filter(Q(object_id=39)) #full_access)
		return
		#q = full_access.filter(Q(object_id=39))
		#print q
					

		return

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


	
