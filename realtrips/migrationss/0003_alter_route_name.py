# Generated by Django 4.2 on 2023-04-10 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtrips', '0002_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='name',
            field=models.CharField(choices=[('Nairobi-Thika', 'Nairobi-Thika'), ('Nairobi-Malaa', 'Nairobi-Malaa'), ('Nairobi-Makongeni', 'Nairobi-Makongeni')], max_length=100),
        ),
    ]
