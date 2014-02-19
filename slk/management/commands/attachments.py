
from treeio.messaging.models import Message, MessageStream
from treeio.identities.models import Contact, ContactType

from django.db.models import Q

import email
import sifter.parser

import datetime

def lcs(word1, word2):

    w1 = set(word1[i:j] for i in range(0, len(word1))
             for j in range(1, len(word1) + 1))

    w2 = set(word2[i:j] for i in range(0, len(word2))
             for j in range(1, len(word2) + 1))

    common_subs = w1.intersection(w2)

    sorted_cmn_subs = sorted([
        (len(str), str) for str in list(common_subs)
        ])

    return sorted_cmn_subs.pop()[1]


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

		import finance.models as finance
		import core.models as models
		from collections import OrderedDict

		uncat = finance.Category.objects.filter(Q(name__startswith="Uncat")).all()[0]

		f = finance.Transaction.objects.filter(Q(category=uncat)).all()
		print len(f)

		words = {}
		for row in f:
			w = row.name.split(' ')
			for word in w:
				if word in words: continue
				if len(word) < 3: continue
				t = finance.Transaction.objects.filter(Q(name__contains=word)).count()
				words[word] = t

		from operator import itemgetter
		d2 = OrderedDict(sorted(words.items(), key=lambda x: x[1], reverse=True))
		for d in d2: print "%s=%d" % (d, d2[d])

		return;

		import csv, math

		file = "/root/biz-3779.csv"
		#file = "/root/personal-0686.csv"
		file = "/root/jointsaving-5556.csv"
		file = "/root/joint-1150.csv"
	
		acct = "3779"
		#acct = "0686"
		acct = "5556"
		acct = "1150"

		#me = Contact.objects.filter(Q(name='Total Travel Marketing, Inc.')).all()[0]
		me = Contact.objects.filter(Q(name="Joseph Fields")).all()[0]

		with open(file, "rb") as csvfile:
			reader = csv.reader(csvfile, delimiter=',', quotechar='"')
			for row in reader:

				f = finance.Transaction()

				if (float(row[1]) < 0):
					f.source = me
					f.target = Contact.objects.filter(Q(name='Unbalanced')).all()[0]
				else:
                                        f.target = me
                                        f.source = Contact.objects.filter(Q(name='Unbalanced')).all()[0]

				f.name = row[4]
				f.account = finance.Account.objects.filter(Q(name=acct)).all()[0]
				f.value = math.fabs(float(row[1]))
				f.datetime = datetime.datetime.strptime(row[0], "%m/%d/%Y")
				f.value_currency = finance.Currency.objects.filter(Q(code="USD")).all()[0]
				f.category = finance.Category.objects.filter(Q(name__startswith="Uncat")).all()[0]
				f.details = row[4]
				f.save()

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


	
