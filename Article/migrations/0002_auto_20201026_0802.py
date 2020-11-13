# Generated by Django 3.1.2 on 2020-10-26 02:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('heading', models.CharField(max_length=200)),
                ('title1', models.CharField(max_length=200)),
                ('title1_Description', models.TextField(blank=True)),
                ('title2', models.CharField(max_length=200)),
                ('title2_Description', models.TextField(blank=True)),
                ('title3', models.CharField(max_length=200)),
                ('title3_Description', models.TextField(blank=True)),
                ('title4', models.CharField(max_length=200)),
                ('title4_Description', models.TextField(blank=True)),
                ('img1', models.ImageField(upload_to='Images')),
                ('img2', models.ImageField(upload_to='Images')),
                ('img3', models.ImageField(upload_to='Images')),
                ('postedby', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='celebrityPost', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Celebrity',
        ),
    ]
