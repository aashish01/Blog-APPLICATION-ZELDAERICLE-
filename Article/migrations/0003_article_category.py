# Generated by Django 3.1.2 on 2020-10-26 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0002_auto_20201026_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('celebrity', 'Celebrity'), ('gadgets', 'Gadgets'), ('destinations', 'Destinations')], default='celibrity', max_length=15),
        ),
    ]
