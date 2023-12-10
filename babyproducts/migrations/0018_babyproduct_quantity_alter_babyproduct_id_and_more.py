# Generated by Django 5.0 on 2023-12-10 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babyproducts', '0017_auto_20231110_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='babyproduct',
            name='quantity',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='babyproduct',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]