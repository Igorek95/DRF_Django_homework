# Generated by Django 5.0 on 2023-12-16 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название курса')),
                ('preview_img', models.ImageField(blank=True, null=True, upload_to='course/', verbose_name='превью (картинка)')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание курса')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название урока')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание урока')),
                ('preview_img', models.ImageField(blank=True, null=True, upload_to='lesson/', verbose_name='превью (картинка)')),
                ('video_link', models.CharField(max_length=250, verbose_name='ссылка на видео')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='курс')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='дата оплаты')),
                ('object_id', models.PositiveIntegerField()),
                ('summ', models.IntegerField(verbose_name='сумма оплаты')),
                ('payment_type', models.CharField(choices=[('cash', 'наличные'), ('card', 'карта')], max_length=4, verbose_name='способ оплаты')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
    ]