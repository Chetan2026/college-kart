# Generated by Django 3.1.2 on 2020-11-21 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='username',
        ),
    ]
