from django.db import migrations
from oc_lettings_site.models import Address as SourceAddress
from ..models import Address as DestinationAddress

class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
    ]

    # Deleting the models, automatically drop the tables too
    operations = [
        migrations.DeleteModel('Letting'),
        migrations.DeleteModel('Address'),
        migrations.DeleteModel('Profile'),
    ]
