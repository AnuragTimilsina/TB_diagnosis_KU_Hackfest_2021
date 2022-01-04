# Generated by Django 3.1.6 on 2022-01-04 04:25

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lungs_status', models.CharField(max_length=30)),
                ('remarks', models.CharField(max_length=200)),
                ('test_date', models.DateTimeField(default=api.models.Record.time_date)),
                ('x_ray', models.CharField(max_length=100)),
                ('confidence', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
