# Generated by Django 3.1.3 on 2020-12-13 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Card_condition',
            field=models.CharField(choices=[('NM', 'NM'), ('LP', 'LP'), ('MP', 'MP'), ('HP', 'HP'), ('D', 'D'), ('None', 'None')], max_length=30),
        ),
        migrations.AlterField(
            model_name='products',
            name='Game_condition',
            field=models.CharField(choices=[('Nw', 'New'), ('LN', 'Like-New'), ('US', 'Used'), ('None', 'None')], max_length=30),
        ),
    ]
