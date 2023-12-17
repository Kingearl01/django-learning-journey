# Generated by Django 4.2.4 on 2023-09-07 15:21

from django.db import migrations
import django_ckeditor_5.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('core', '0025_alter_productreview_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, default='I"m amazing Vendor', null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='product',
            name='specifications',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, default='It is specidication', null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, default='I"m amazing Vendor', null=True, verbose_name='Text'),
        ),
    ]
