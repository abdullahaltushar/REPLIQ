# Generated by Django 4.1.7 on 2023-04-03 05:59

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
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('serial_number', models.CharField(max_length=255, unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.company')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_time', models.DateTimeField()),
                ('return_time', models.DateTimeField(blank=True, null=True)),
                ('checkout_condition', models.CharField(blank=True, max_length=255, null=True)),
                ('return_condition', models.CharField(blank=True, max_length=255, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.device')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.employee')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='employees',
            field=models.ManyToManyField(through='demo.DeviceLog', to='demo.employee'),
        ),
    ]
