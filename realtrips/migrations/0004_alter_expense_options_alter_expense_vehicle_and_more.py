# Generated by Django 4.2 on 2023-04-12 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtrips', '0003_alter_route_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterField(
            model_name='expense',
            name='Vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='realtrips.vehicle'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='realtrips.profile'),
        ),
        migrations.AlterField(
            model_name='route',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='vehicle',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='realtrips.vehicle'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='Vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='realtrips.vehicle'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='realtrips.profile'),
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='realtrips.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='realtrips.profile')),
            ],
        ),
    ]
