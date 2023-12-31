# Generated by Django 4.1.4 on 2023-07-09 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0054_lawyer_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client_signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_full_name', models.CharField(max_length=255)),
                ('client_email', models.EmailField(max_length=255)),
                ('client_password', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='UserClients',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
