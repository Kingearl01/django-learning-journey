# Generated by Django 4.2.3 on 2023-07-17 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_rename_studentid_results_indexnumber_results_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='title',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='account.courses'),
        ),
    ]
