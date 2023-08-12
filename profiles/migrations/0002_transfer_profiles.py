from django.db import migrations
from oc_lettings_site.models import Profile as SourceProfile
from ..models import Profile as DestinationProfile

def transfer_profiles(apps, schema_editor):
    for profile in SourceProfile.objects.all():
        DestinationProfile.objects.create(
            favorite_city=profile.favorite_city,
            user_id=profile.user.id
        )

def reverse_func(apps, schema_editor):
    DestinationProfile.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    # https://stackoverflow.com/questions/66479161/what-does-runpython-noop-do
    operations = [
        migrations.RunPython(
            code=transfer_profiles,
            reverse_code=reverse_func
        )
    ]
