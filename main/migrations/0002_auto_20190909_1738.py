# Generated by Django 2.2.5 on 2019-09-09 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outdoordate',
            old_name='location',
            new_name='place',
        ),
    ]
