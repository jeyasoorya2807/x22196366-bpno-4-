# Generated by Django 5.0 on 2024-04-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babyproducts', '0021_babyproduct_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babyproduct',
            name='image',
            field=models.ImageField(default='null', upload_to='images'),
        ),
    ]
