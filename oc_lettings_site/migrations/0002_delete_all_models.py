from django.db import migrations


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
