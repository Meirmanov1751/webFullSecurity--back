# Generated by Django 4.2 on 2023-04-18 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_delete_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]
