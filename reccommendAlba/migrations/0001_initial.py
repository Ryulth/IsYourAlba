# Generated by Django 2.1.3 on 2018-11-23 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OHaeng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.CharField(max_length=10, verbose_name='Birth Date')),
                ('tree', models.IntegerField(max_length=10, verbose_name='Tree')),
                ('fire', models.IntegerField(max_length=10, verbose_name='Tree')),
                ('soil', models.IntegerField(max_length=10, verbose_name='Tree')),
                ('metal', models.IntegerField(max_length=10, verbose_name='Tree')),
                ('water', models.IntegerField(max_length=10, verbose_name='Tree')),
            ],
        ),
    ]
