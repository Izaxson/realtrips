# Generated by Django 4.2 on 2023-05-08 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtrips', '0016_alter_expense_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='fleet_no',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='realtrips.profile'),
            preserve_default=False,
        ),
    ]
