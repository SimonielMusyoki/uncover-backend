# Generated by Django 4.2.6 on 2023-10-21 11:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_product_orders_count_alter_product_quantity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductImages',
            new_name='ProductImage',
        ),
        migrations.RenameModel(
            old_name='Ratings',
            new_name='Rating',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='rating',
            new_name='average_rating',
        ),
    ]
