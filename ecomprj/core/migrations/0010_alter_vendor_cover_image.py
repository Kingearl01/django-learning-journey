# Generated by Django 4.2.4 on 2023-09-04 11:49

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_vendor_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='cover_image',
            field=models.ImageField(default='media/user 11/vendor-header-bg.png', upload_to=core.models.user_directory_path),
        ),
    ]