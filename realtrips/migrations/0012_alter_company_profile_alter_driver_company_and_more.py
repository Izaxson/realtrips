# Generated by Django 4.1.7 on 2023-04-12 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtrips', '0011_alter_company_profile_alter_driver_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='realtrips.profile'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='driver', to='realtrips.company'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='realtrips.company'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='realtrips.company'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='profilevehicle', to='realtrips.profile'),
        ),
    ]
