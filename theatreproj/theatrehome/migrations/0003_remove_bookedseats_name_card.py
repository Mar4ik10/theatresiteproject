# Generated by Django 4.2.6 on 2023-12-20 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theatrehome', '0002_auto_20231220_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookedseats',
            name='name_card',
        ),
    ]