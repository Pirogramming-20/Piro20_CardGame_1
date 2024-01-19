# Generated by Django 5.0.1 on 2024-01-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_choice', models.IntegerField(verbose_name='플레이어 A 선택 숫자')),
                ('b_choice', models.IntegerField(blank=True, null=True, verbose_name='플레이어 B 선택 숫자')),
                ('rule', models.IntegerField(verbose_name='랜덤 규칙')),
                ('winner', models.CharField(blank=True, default=None, max_length=16, null=True)),
            ],
        ),
    ]
