# Generated by Django 4.2.4 on 2023-08-15 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='raiting',
            name='user',
            field=models.ManyToManyField(related_name='raitings', to=settings.AUTH_USER_MODEL, verbose_name='Участники рейтинга'),
        ),
        migrations.AddField(
            model_name='order',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.chat', verbose_name='Чат'),
        ),
        migrations.AddField(
            model_name='order',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='services.service', verbose_name='Услуга в заказе'),
        ),
        migrations.AddField(
            model_name='order',
            name='users',
            field=models.ManyToManyField(related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Участники сделки'),
        ),
        migrations.AddField(
            model_name='message',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL, verbose_name='Участник чата'),
        ),
        migrations.AddField(
            model_name='chat',
            name='users',
            field=models.ManyToManyField(related_name='chats', to=settings.AUTH_USER_MODEL, verbose_name='Участники чата'),
        ),
    ]
