# Generated by Django 2.1.15 on 2023-11-10 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('babyproducts', '0016_auto_20231110_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='babyproducts.Babyproduct'),
        ),
    ]
