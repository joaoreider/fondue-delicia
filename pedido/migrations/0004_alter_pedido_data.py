# Generated by Django 4.1.4 on 2022-12-26 23:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_pedido_cupom_alter_pedido_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 26, 20, 0, 17, 363294)),
        ),
    ]