# Generated by Django 2.0.8 on 2022-07-28 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myform', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cost',
            name='date_of_creation',
        ),
    ]