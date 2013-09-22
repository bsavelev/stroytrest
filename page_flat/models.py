# -*- coding:utf-8 -*-
from django.db import models
from common.models import SystemMixin
from seo.models import SeoMetaTags


class Flat(SeoMetaTags, SystemMixin):
    """
    Статические страницы

    Поля:
    url - путь, урл страницы
    title - заголовок страницы
    text - текст страницы
    """

    url = models.URLField(u'Ссылка')
    title = models.CharField(u'Заголовок', max_length=250)
    text = models.TextField(u'Текст')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Статические страницы'
        verbose_name_plural = u'Статические страницы'