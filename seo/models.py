# -*- coding:utf-8 -*-
from django.db import models


class SeoMetaTags(models.Model):
    """
    Родительская модель для сео, Мета теги и title

    Поля:
    seo_title - title страницы
    seo_description - мета тег description
    seo_keywords - мета тег keywords
    """

    seo_title = models.CharField(u'Title', max_length=100)
    seo_description = models.CharField(u'Description', max_length=250)
    seo_keywords = models.CharField(u'Keywords', max_length=250)

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'СЕО мета-теги'
        verbose_name_plural = u'СЕО мета-теги'