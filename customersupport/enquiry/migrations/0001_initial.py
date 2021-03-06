# Generated by Django 3.2 on 2021-04-19 05:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255, validators=[django.core.validators.RegexValidator('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$)', 'Enter a valid email address.')])),
                ('mobile', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^[789]\\d{9}$', 'Invalid contact number.')], verbose_name='Mobile No.')),
                ('query', models.TextField()),
            ],
            options={
                'db_table': 'enquiry',
            },
        ),
    ]
