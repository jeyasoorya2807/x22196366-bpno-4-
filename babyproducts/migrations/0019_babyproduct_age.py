# Generated by Django 5.0 on 2024-03-27 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babyproducts', '0018_babyproduct_quantity_alter_babyproduct_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='babyproduct',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]