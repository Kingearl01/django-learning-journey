# Generated by Django 4.2.3 on 2023-07-17 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_results_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
        migrations.RenameModel(
            old_name='Results',
            new_name='Result',
        ),
    ]
