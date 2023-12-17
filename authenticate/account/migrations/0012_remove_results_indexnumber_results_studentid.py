# Generated by Django 4.2.3 on 2023-07-17 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_rename_coursecode_courses_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='indexnumber',
        ),
        migrations.AddField(
            model_name='results',
            name='studentid',
            field=models.ForeignKey(blank=True, default='200048402', on_delete=django.db.models.deletion.CASCADE, to='account.student'),
        ),
    ]
