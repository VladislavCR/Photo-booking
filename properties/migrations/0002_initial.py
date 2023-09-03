# Generated by Django 4.2.4 on 2023-09-03 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='properties', to=settings.AUTH_USER_MODEL, verbose_name='Владелец недвижимости'),
        ),
        migrations.AddField(
            model_name='feedbackproperty',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedback_properties', to='properties.property', verbose_name='Название недвижимости'),
        ),
        migrations.AddField(
            model_name='feedbackproperty',
            name='user_client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedback_properties', to=settings.AUTH_USER_MODEL, verbose_name='Клиент'),
        ),
    ]
