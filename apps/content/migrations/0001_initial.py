# Generated by Django 4.2.6 on 2023-10-21 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0002_product_orders_count_alter_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlyoutMenuItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=15)),
                ('landing_page', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='HomepageSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Image Name')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('landing_page', models.URLField(verbose_name='URL')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Page Name')),
                ('landing_page', models.SlugField()),
                ('seo_text', models.TextField(max_length=50, verbose_name='SEO Text')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='')),
                ('page_html', models.TextField(verbose_name='HTML Code')),
                ('featured_products', models.ManyToManyField(to='store.product', verbose_name='Products on the page')),
            ],
        ),
        migrations.CreateModel(
            name='HomepageProductFloor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Title')),
                ('landing_page', models.URLField(blank=True, null=True, verbose_name='Landing page')),
                ('has_countdown', models.BooleanField(default=False, verbose_name='Enable countdown')),
                ('countdown_enddate', models.DateTimeField(blank=True, null=True, verbose_name='Countdown End Time')),
                ('active', models.BooleanField(default=True, verbose_name='Activate')),
                ('products', models.ManyToManyField(to='store.product', verbose_name='Products on this widget')),
            ],
        ),
    ]
