# Generated by Django 4.2.4 on 2023-09-03 07:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Название чата')),
            ],
            options={
                'verbose_name': 'Чат',
                'verbose_name_plural': 'Чаты',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст сообщения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ('author',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Название заказа')),
                ('cost', models.PositiveIntegerField(verbose_name='Стоимость заказа')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата заказа')),
                ('completion_date', models.DateTimeField(verbose_name='Время исполнения')),
                ('status', models.BooleanField(default=False, verbose_name='Статус выполнения заказа')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Raiting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raiting', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Оценка исполнителя')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='raitings', to='orders.order', verbose_name='')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
                'ordering': ('order',),
            },
        ),
    ]