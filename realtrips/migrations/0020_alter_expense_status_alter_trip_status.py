# Generated by Django 4.2.2 on 2023-06-30 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtrips', '0019_expense_status_trip_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='trip',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
