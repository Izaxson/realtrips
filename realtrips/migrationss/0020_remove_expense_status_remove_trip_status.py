# Generated by Django 4.2.2 on 2023-07-09 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtrips', '0019_expense_status_trip_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='status',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='status',
        ),
    ]