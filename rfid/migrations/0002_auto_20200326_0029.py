# Generated by Django 3.0.4 on 2020-03-26 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfid',
            name='idalumno',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
