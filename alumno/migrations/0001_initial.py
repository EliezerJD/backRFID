# Generated by Django 2.2.7 on 2019-11-20 18:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ap_pat', models.CharField(max_length=100)),
                ('ap_mat', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('idrfid', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'alumno',
            },
        ),
    ]
