# Generated by Django 4.1.6 on 2023-03-07 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_item_category_item_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='test-product'),
        ),
    ]
