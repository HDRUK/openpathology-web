# Generated by Django 2.2 on 2019-07-22 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_measure'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='boundary',
        ),
        migrations.RemoveField(
            model_name='practice',
            name='boundary',
        ),
        migrations.RemoveField(
            model_name='practice',
            name='location',
        ),
    ]
