# Generated by Django 5.0.3 on 2024-03-06 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='time',
            new_name='date',
        ),
    ]
