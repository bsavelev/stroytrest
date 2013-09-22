# -*- coding:utf-8 -*-
from django.db import models
from common.models import SystemMixin
from common.models import get_upload_to_path


def get_upload_path(instance, filename):
    """
    Получение пути для сохранения логотипа
    """
    return get_upload_to_path(instance, filename, 'slider')


class Slider(models.Model, SystemMixin):
    """
    Слайдер на главной

    Поля:
    img - картинка слайдера
    url - ссылка на страницу с картинки
    slider_order - порядок слайдеров
    """

    img = models.ImageField(u'Картинка', upload_to=get_upload_path)
    url = models.URLField(u'Ссылка')
    slider_order = models.PositiveSmallIntegerField(u'Порядок')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Слайдер'
        verbose_name_plural = u'Слайдер'
        ordering = ['slider_order']