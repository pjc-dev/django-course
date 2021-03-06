# Generated by Django 2.1.7 on 2021-02-03 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
