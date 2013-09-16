# -*- coding:utf-8 -*-
from django.db import models
from common.models import get_upload_to_path


def get_upload_path(instance, filename):
    """
    Получение пути для сохранения логотипа
    """
    return get_upload_to_path(instance, filename, 'logo')


class StaticValues(models.Model):
    """
    Статические переменные (адрес, контакты, телефон, логотип)

    Поля:
    address - адрес компании
    telefon - телефон компании
    hours_of_operation - часы работы компании
    logo - логотип
    slogan - слоган
    """

    address = models.CharField(u'Адрес', max_length=250)
    telefon = models.CharField(u'Телефон', max_length=25)
    hours_of_operation = models.CharField(u'Часы работы', max_length=200)
    logo = models.ImageField(u'Логотип', upload_to=get_upload_path)
    slogan = models.CharField(u'Слоган', max_length=250)

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Статические данные'
        verbose_name_plural = u'Статичесике данные'