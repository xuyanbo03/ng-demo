# Generated by Django 3.0.5 on 2020-04-28 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200415_2206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderinfo',
            old_name='oder_id',
            new_name='order_id',
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='comment',
            field=models.CharField(default='', max_length=256, verbose_name='评论'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='trade_no',
            field=models.CharField(default='', max_length=128, verbose_name='支付编号'),
        ),
    ]