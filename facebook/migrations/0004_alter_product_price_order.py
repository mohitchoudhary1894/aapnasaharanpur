# Generated by Django 4.0.6 on 2022-09-05 02:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0003_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=220)),
                ('mobile_no', models.BigIntegerField()),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('date', models.DateTimeField(verbose_name=datetime.datetime)),
                ('status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facebook.registration')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facebook.product')),
            ],
        ),
    ]
