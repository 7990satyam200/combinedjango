# Generated by Django 2.0 on 2018-06-13 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Network', '0002_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='tweet',
        ),
    ]
