# Generated by Django 4.2.4 on 2023-08-15 19:08

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone
import phone_field.models
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media_file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(verbose_name='Ссылка на медиа файл')),
                ('title', models.CharField(max_length=25, verbose_name='Название')),
                ('media_type', models.CharField(max_length=25, verbose_name='Тип медиа файла')),
                ('is_main_photo', models.BooleanField(verbose_name='Отображение файла на главной')),
            ],
            options={
                'verbose_name': 'Медиа файл',
                'verbose_name_plural': 'Медиа файлы',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=25, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('username', models.CharField(max_length=150, unique=True, validators=[users.validators.CorrectUsernameAndNotMe], verbose_name='username')),
                ('profile_photo', models.ImageField(blank=True, upload_to='users/profile', verbose_name='Фото профиля')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта для регистрации')),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта для связи')),
                ('phone', phone_field.models.PhoneField(help_text='Телефон для контакта', max_length=31, unique=True, verbose_name='Номер телефона')),
                ('work_experience', models.FloatField(default=0, verbose_name='Опыт работы')),
                ('city', models.CharField(help_text='Укажите город проживания', max_length=25, verbose_name='Город')),
                ('raiting', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Рейтинг профиля')),
                ('about_me', models.TextField(max_length=500, verbose_name='Обо мне')),
                ('is_photographer', models.BooleanField(default=False, verbose_name='Роль.Фотограф')),
                ('is_video_operator', models.BooleanField(default=False, verbose_name='Роль.Видео-оператор')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='День рождения')),
                ('social', models.URLField(blank=True, null=True, verbose_name='Социальные сети')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('servicies', models.ManyToManyField(related_name='users', to='services.service', verbose_name='Услуги')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('email',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
