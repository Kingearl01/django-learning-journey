# Generated by Django 4.2.3 on 2023-08-19 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='image.jpg', upload_to='featured_image/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
