# Generated by Django 4.2.2 on 2023-06-28 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_appointment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='date',
            new_name='dates',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='email',
            new_name='emails',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='message',
            new_name='messages',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='name',
            new_name='names',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='pdf',
            new_name='pdfs',
        ),
    ]
