# Generated by Django 3.1.6 on 2021-02-20 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='x_ray',
            field=models.CharField(max_length=100),
        ),
    ]
