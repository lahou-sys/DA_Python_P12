# Generated by Django 4.0.4 on 2022-06-05 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
