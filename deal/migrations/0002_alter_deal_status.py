# Generated by Django 4.0.6 on 2022-07-12 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='status',
            field=models.PositiveIntegerField(choices=[('거래 종료', '거래 종료'), ('거래 가능', '거래 가능'), ('예약 중', '예약 중'), ('거래 중', '거래 중')], verbose_name='상태'),
        ),
    ]
