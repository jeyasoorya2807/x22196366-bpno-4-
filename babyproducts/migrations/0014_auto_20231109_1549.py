# Generated by Django 2.1.15 on 2023-11-09 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('babyproducts', '0013_auto_20231109_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='babyproducts.Babyproduct'),
        ),
    ]
