# Generated by Django 3.2.7 on 2021-12-21 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(default='female', max_length=100),
            preserve_default=False,
        ),
    ]