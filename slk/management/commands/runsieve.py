
from treeio.messaging.models import Message
from django.db.models import Q

def Command():
	print "hello"
	m = Message.objects.filter(Q(author=78)).count()
	print m

	
