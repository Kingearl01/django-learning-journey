# Generated by Django 4.2.3 on 2023-07-17 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_student_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='index_number',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]