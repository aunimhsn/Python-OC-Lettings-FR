from django.db import migrations
from oc_lettings_site.models import Letting as SourceLetting
from ..models import Letting as DestinationLetting

def transfer_lettings(apps, schema_editor):
    for letting in SourceLetting.objects.all():
        DestinationLetting.objects.create(
            title=letting.title,
            address_id=letting.address.id
        )

class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_transfer_addresses'),
    ]

    operations = [
        migrations.RunPython(transfer_lettings)
    ]
