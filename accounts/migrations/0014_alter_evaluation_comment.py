# Generated by Django 4.0 on 2022-08-27 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_evaluation_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='comment',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
