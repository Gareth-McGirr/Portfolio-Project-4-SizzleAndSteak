# Generated by Django 4.0.5 on 2022-06-17 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='gluten_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu_item_type',
            field=models.CharField(choices=[('starter', 'Starter'), ('main', 'Main'), ('desert', 'Desert'), ('drink', 'Drink'), ('side', 'Side')], default='starter', max_length=25),
        ),
    ]
