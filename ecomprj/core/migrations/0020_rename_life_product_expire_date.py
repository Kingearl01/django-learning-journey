# Generated by Django 4.2.4 on 2023-09-04 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_product_stock_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='life',
            new_name='expire_date',
        ),
    ]
