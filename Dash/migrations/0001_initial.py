# Generated by Django 3.0.7 on 2020-07-03 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('device_name', models.TextField(max_length=60)),
                ('location_id', models.CharField(max_length=60)),
                ('device_type', models.CharField(max_length=60)),
            ],
        ),
    ]
