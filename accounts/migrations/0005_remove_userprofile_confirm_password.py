# Generated by Django 4.1.7 on 2023-03-13 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userprofile_confirm_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='confirm_password',
        ),
    ]