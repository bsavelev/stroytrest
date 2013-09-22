# -*- coding:utf-8 -*-
from django.db import models
from common.models import SystemMixin
from seo.models import SeoMetaTags


class News(SeoMetaTags, SystemMixin):
    """
    Новости

    Поля:
    url - ссылка на новость
    title - заголовок новости
    text - текст новости
    """

    url = models.URLField(u'Ссылка')
    title = models.CharField(u'Заголовок', max_length=250)
    text = models.TextField(u'Текст')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'