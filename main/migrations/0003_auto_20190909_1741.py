# Generated by Django 2.2.5 on 2019-09-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190909_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outdoordate',
            name='comments',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
