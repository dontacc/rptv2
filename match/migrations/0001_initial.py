# Generated by Django 3.2.16 on 2022-11-12 14:56

import django.core.validators
from django.db import migrations, models


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
                ('phone', models.CharField(max_length=11, unique=True)),
                ('phone2', models.CharField(blank=True, max_length=11, null=True, unique=True)),
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
                ('phone', models.CharField(max_length=11, unique=True)),
            ],
        ),
    ]
