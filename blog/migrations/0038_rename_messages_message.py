# Generated by Django 4.2.2 on 2023-06-29 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_messages_delete_message'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messages',
            new_name='Message',
        ),
    ]
