# Generated by Django 3.2.6 on 2022-05-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlShort', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmodel',
            name='shorturl',
            field=models.CharField(max_length=5),
        ),
    ]
