# Generated by Django 4.1.1 on 2022-10-31 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_user_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='active_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]
