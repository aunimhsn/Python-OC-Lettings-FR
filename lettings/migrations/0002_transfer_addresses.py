from django.db import migrations
from oc_lettings_site.models import Address as SourceAddress
from ..models import Address as DestinationAddress

def transfer_addresses(apps, schema_editor):
    for address in SourceAddress.objects.all():
        DestinationAddress.objects.create(
            number=address.number,
            street=address.street,
            city=address.city,
            state=address.state,
            zip_code=address.zip_code,
            country_iso_code=address.country_iso_code
        )

class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(transfer_addresses),
    ]
