# Generated by Django 4.2.2 on 2023-06-29 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_remove_message_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='names',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
