# Generated by Django 2.2.16 on 2021-11-11 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_auto_20211110_2243'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follow',
        ),
    ]