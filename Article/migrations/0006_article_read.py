# Generated by Django 3.1.2 on 2020-10-28 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0005_auto_20201028_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='read',
            field=models.IntegerField(default=0),
        ),
    ]
