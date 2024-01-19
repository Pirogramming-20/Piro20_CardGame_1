# Generated by Django 5.0.1 on 2024-01-19 06:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='player_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_a', to=settings.AUTH_USER_MODEL, verbose_name='플레이어 A'),
        ),
        migrations.AddField(
            model_name='game',
            name='player_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_b', to=settings.AUTH_USER_MODEL, verbose_name='플레이어 B'),
        ),
    ]
