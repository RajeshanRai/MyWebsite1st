# Generated by Django 3.2.6 on 2021-08-22 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='title',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personal',
            name='upload',
            field=models.FileField(default=1, upload_to='media'),
            preserve_default=False,
        ),
    ]
