# Generated by Django 4.0.3 on 2022-03-14 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
