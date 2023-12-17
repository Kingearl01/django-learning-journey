# Generated by Django 4.2.4 on 2023-08-28 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to='profile_pic/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/blog/%Y/%m/%d/'),
        ),
    ]