# Generated by Django 4.2.2 on 2023-07-08 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0047_alter_userprofile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserClients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
            ],
        ),
    ]