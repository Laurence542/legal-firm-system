# Generated by Django 4.2.2 on 2023-06-29 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0043_remove_message_names_remove_message_receiver_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_legal', models.TextField(blank=True, null=True)),
                ('timestamp_legal', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
