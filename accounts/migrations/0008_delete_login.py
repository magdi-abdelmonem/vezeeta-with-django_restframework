# Generated by Django 4.0 on 2022-08-22 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_login_alter_profile_specialization_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
    ]
