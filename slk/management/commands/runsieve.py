
from treeio.messaging.models import Message
from treeio.identities.models import Contact, ContactType

from django.db.models import Q

def Command():
	print "hello"
	#m = Message.objects.filter(Q(author=78)).count()

	c = Contact.objects.filter(Q(id=109)).all()[0]
	c.contact_type = ContactType.objects.get(Q(name='Person'))
        c.save()


	
