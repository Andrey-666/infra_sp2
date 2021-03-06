# Generated by Django 2.2.16 on 2021-12-07 16:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20211206_1344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-id',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('pub_date',), 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('-id',), 'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('-id',), 'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='Укажите слаг', unique=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(help_text='Укажите автора', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, help_text='Дата публикации', verbose_name='Укажите дату публикации'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(help_text='Оставьте свой отзыв', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.Review', verbose_name='Отзыв'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(help_text='Введите текст комментария', max_length=150, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(help_text='Укажите слаг', unique=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, help_text='Дата публикации', verbose_name='Укажите дату публикации'),
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(error_messages={'validators': 'Оценка может быть от 1 до 10'}, help_text='Укажите оценку произведения', validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.CharField(help_text='Введите текст', max_length=200, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(db_index=True, help_text='Введи название произведения', max_length=200, verbose_name='Произведение'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.SmallIntegerField(blank=True, help_text='Введите год выпуска', validators=[reviews.validators.validate_year], verbose_name='Год выпуска'),
        ),
    ]
