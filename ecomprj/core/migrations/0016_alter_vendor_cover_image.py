# Generated by Django 4.2.4 on 2023-09-04 12:17

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_vendor_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='cover_image',
            field=models.ImageField(default='cover_image.jpg', upload_to=core.models.user_directory_path),
        ),
    ]
