# Generated by Django 4.0.1 on 2022-01-22 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costsplit', '0004_alter_plan_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='creation_date',
        ),
    ]