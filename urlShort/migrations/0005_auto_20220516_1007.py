# Generated by Django 3.2.6 on 2022-05-16 10:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urlShort', '0004_urlmodel_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlmodel',
            name='ip_address',
        ),
        migrations.RemoveField(
            model_name='urlmodel',
            name='location',
        ),
        migrations.CreateModel(
            name='url_analytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(blank=True, max_length=32, null=True)),
                ('location', models.CharField(blank=True, max_length=500, null=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 5, 16, 10, 7, 43, 916805))),
                ('browser', models.CharField(blank=True, max_length=500, null=True)),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urlShort.urlmodel')),
            ],
        ),
    ]