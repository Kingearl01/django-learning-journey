# Generated by Django 4.2.4 on 2023-09-04 10:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_product_category_alter_productreview_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
