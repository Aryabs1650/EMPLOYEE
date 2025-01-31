# Generated by Django 4.1 on 2024-05-06 06:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_number', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('resolution_end_date', models.DateTimeField(blank=True, null=True)),
                ('assigned_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task2.employee')),
            ],
        ),
        migrations.CreateModel(
            name='DutyRoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('is_available', models.BooleanField(default=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task2.employee')),
            ],
        ),
    ]
