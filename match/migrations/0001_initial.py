# Generated by Django 4.1.1 on 2022-10-30 01:00

import django.core.validators
from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipateForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('id_card', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$')])),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('W', 'Woman'), ('M', 'Man')], default='-', max_length=1)),
                ('degree', models.CharField(max_length=200)),
                ('major', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', phone_field.models.PhoneField(max_length=31, unique=True)),
                ('phone2', phone_field.models.PhoneField(max_length=31, unique=True)),
                ('image', models.ImageField(upload_to='match/profile')),
            ],
        ),
        migrations.CreateModel(
            name='VeiwerForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('W', 'Woman'), ('M', 'Man')], default='-', max_length=1)),
                ('city', models.CharField(max_length=200)),
                ('birth_date', models.DateField()),
                ('id_card', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$')])),
                ('phone', phone_field.models.PhoneField(max_length=31, unique=True)),
            ],
        ),
    ]
