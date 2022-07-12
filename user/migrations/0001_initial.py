# Generated by Django 4.0.6 on 2022-07-12 17:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='이메일')),
                ('nickname', models.CharField(max_length=15, unique=True, verbose_name='닉네임')),
                ('password', models.CharField(max_length=256, verbose_name='비밀번호')),
                ('address', models.TextField(max_length=256, verbose_name='주소')),
                ('image', models.FileField(null=True, upload_to='develop/', verbose_name='프로필')),
                ('score', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='유저 점수')),
                ('join_date', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
                ('is_active', models.BooleanField(default=True, verbose_name='계정 활성화 여부')),
                ('is_admin', models.BooleanField(default=False, verbose_name='관리자 권한')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
