from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Text(models.Model):
    text = models.TextField('Текст')

    def __str__(self):
        return self.text[:]

    class Meta:
        verbose_name = 'Глобальный текст'
        verbose_name_plural = 'Глобальный текст'


class News(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    text = models.ForeignKey(
        Text, related_name='news', on_delete=models.CASCADE, null=False, verbose_name='Текст'
    )
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date']




class Timetable(models.Model):
    day = models.CharField('День', max_length=50)
    text = models.ForeignKey(
        Text, related_name='timetable', on_delete=models.CASCADE, null=False, verbose_name='Расписание'
    )

    def __str__(self):
        return self.day

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'



class Refences(models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.ForeignKey(
        Text, related_name='refences', on_delete=models.CASCADE, null=False, verbose_name='Текст'
    )
    user = models.ForeignKey(
        User, related_name='user', on_delete=models.CASCADE, null=False, verbose_name='Индефикатор пользователя'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
