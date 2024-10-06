# yatube_api/posts/models.py

from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import MAX_TEXT_LENGTH, MAX_TITLE_LENGTH

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        verbose_name='Заголовок'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Индификатор'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title[:MAX_TEXT_LENGTH]


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Картинка'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        default_related_name = 'posts'

    def __str__(self):
        return self.text[:MAX_TEXT_LENGTH]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Публикация'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата добавления'
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        default_related_name = 'comments'

    def __str__(self):
        return (
            f'Комментарий к посту {self.post} от {self.author}: '
            f'{self.text[:MAX_TEXT_LENGTH]}'
        )
