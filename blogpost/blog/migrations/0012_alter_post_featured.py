# Generated by Django 4.2.3 on 2023-08-12 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
