# Generated by Django 4.0.6 on 2022-07-28 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_chatroom_receiver_remove_chatroom_sender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='application',
            field=models.BooleanField(default=False, verbose_name='신청'),
        ),
    ]
