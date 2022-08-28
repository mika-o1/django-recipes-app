# Generated by Django 4.0.4 on 2022-08-28 20:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Заголовок', help_text='<small class="text-muted">это наш заголовок</small><hr><br>', max_length=250, null=True, verbose_name='Заголовок:')),
                ('image', models.ImageField(blank=True, default='img/receipt/default/default_receipt.jpg', help_text='<small class="text-muted">это наша заставка</small><hr><br>', null=True, upload_to='img/receipt', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])], verbose_name='Заставка:')),
                ('time_to_cook', models.IntegerField(blank=True, default='1', help_text='<small class="text-muted">это наше время на приготовление</small><hr><br>', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)], verbose_name='Время на приготовление(минуты)')),
                ('description', models.TextField(default='Описание', help_text='<small class="text-muted">это наше Описание</small><hr><br>', verbose_name='Описание:')),
                ('is_completed', models.BooleanField(default=False)),
                ('instructions', models.FileField(blank=True, default=None, help_text='<small class="text-muted">Инструкция</small><hr><br>', null=True, upload_to='file/pdf', validators=[django.core.validators.FileExtensionValidator(['PDF', 'XLSX'])], verbose_name='Инструкция:')),
                ('author', models.ForeignKey(blank=True, default=None, error_messages=False, help_text='<small class="text-muted">автор</small><hr><br>', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, unique_for_date=False, unique_for_month=False, unique_for_year=False, verbose_name='Автор блюда')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ('title', 'description'),
            },
        ),
        migrations.CreateModel(
            name='ReceiptCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Заголовок', help_text='<small class="text-muted">это наш заголовок</small><hr><br>', max_length=250, null=True, verbose_name='Заголовок:')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории рецептов',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='ReceiptIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='Название', help_text='<small class="text-muted">это наше название</small><hr><br>', null=True, verbose_name='Название:')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ReceiptRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_liked', models.BooleanField(blank=True, default=False, help_text='<small class="text-muted">Лайк</small><hr><br>', null=True, verbose_name='Лайк:')),
                ('rating_value', models.IntegerField(blank=True, default='0', help_text='<small class="text-muted">Оценка</small><hr><br>', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Оценка')),
                ('receipt', models.ForeignKey(blank=True, default=None, error_messages=False, help_text='<small class="text-muted">Рецепт</small><hr><br>', null=True, on_delete=django.db.models.deletion.CASCADE, to='app_teacher.receipt', unique_for_date=False, unique_for_month=False, unique_for_year=False, verbose_name='Рецепт')),
                ('user', models.ForeignKey(blank=True, default=None, error_messages=False, help_text='<small class="text-muted">Пользователь</small><hr><br>', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique_for_date=False, unique_for_month=False, unique_for_year=False, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Рейтинг рецепта',
                'verbose_name_plural': 'Рейтинги рецептов',
                'ordering': ('receipt',),
            },
        ),
        migrations.CreateModel(
            name='ReceiptComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(blank=True, default='Текст комментария', help_text='<small class="text-muted">Текст комментария</small><hr><br>', max_length=500, null=True, verbose_name='Заголовок:')),
                ('time', models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='<small class="text-muted">время создания</small><hr><br>', null=True, verbose_name='время создания:')),
                ('create', models.DateTimeField(auto_now_add=True, help_text='<small class="text-muted">время создания</small><hr><br>', null=True, verbose_name='время создания:')),
                ('update', models.DateTimeField(auto_now=True, help_text='<small class="text-muted">время создания</small><hr><br>', null=True, verbose_name='время создания:')),
                ('receipt', models.ForeignKey(blank=True, default=None, error_messages=False, help_text='<small class="text-muted">Рецепт</small><hr><br>', null=True, on_delete=django.db.models.deletion.CASCADE, to='app_teacher.receipt', unique_for_date=False, unique_for_month=False, unique_for_year=False, verbose_name='Рецепт')),
                ('user', models.ForeignKey(blank=True, default=None, error_messages=False, help_text='<small class="text-muted">Пользователь</small><hr><br>', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, unique_for_date=False, unique_for_month=False, unique_for_year=False, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий к рецепту',
                'verbose_name_plural': 'Комментарии к рецептам',
                'ordering': ('-time',),
            },
        ),
        migrations.AddField(
            model_name='receipt',
            name='category',
            field=models.ManyToManyField(blank=True, db_column='country_db_column', db_index=True, default=None, error_messages=False, help_text='<small class="text-muted">категория</small><hr><br>', to='app_teacher.receiptcategory', unique_for_date=False, unique_for_month=False, unique_for_year=False, verbose_name='Категория блюда'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='ingredients',
            field=models.ManyToManyField(blank=True, default=None, help_text='<small class="text-muted">ингредиенты</small><hr><br>', to='app_teacher.receiptingredient', verbose_name='Ингредиенты блюда'),
        ),
    ]
