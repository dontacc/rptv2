# Generated by Django 4.1.1 on 2022-10-31 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_user_active_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active_code',
            field=models.CharField(default='1234', max_length=6),
            preserve_default=False,
        ),
    ]