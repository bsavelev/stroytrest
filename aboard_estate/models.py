# -*- coding:utf-8 -*-
from django.db import models
from common.models import SystemMixin, PhotoMeta, PriceMixin
from apartment.models import NumberOfRooms, Toilet
from commercial_estate.models import CommunicationsWithInternet
from seo.models import SeoMetaTags


class AboardEstate(SeoMetaTags, SystemMixin, PriceMixin):
    """
    Зарубежная недвижимость

    Поля:
    sale - продажа? или аренда
    country - страна
    area - общая плошадь
    rooms - комнаты
    communications - комуникации
    toilet - сан. узел
    """

    sale = models.BooleanField(u'Продажа? или аренда')
    country = models.ForeignKey('Country', verbose_name=u'Страна', related_name='aboardestate_country_related')
    area = models.DecimalField(u'Общая площадь', max_digits=6, decimal_places=2)
    rooms = models.ForeignKey(NumberOfRooms,
                              verbose_name=u'Количество комнат',
                              related_name='aboardestate_rooms_related')
    communications = models.ForeignKey(CommunicationsWithInternet,
                                       verbose_name=u'Комуникации',
                                       related_name='aboardestate_communications_related')
    toilet = models.ForeignKey(Toilet, verbose_name=u'Сан. узел', related_name='aboardestate_toilet_related')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Зарубежная недвижимость'
        verbose_name_plural = u'Зарубежная недвижимость'


class PhotoAboardEstate(PhotoMeta):
    """
    Фото зарубежной недвижимости

    Поля:
    aboard_estate - объект зарубежной недвижимости
    """

    aboard_estate = models.ForeignKey('AboardEstate',
                                      verbose_name=u'Зарубежная недвижимость',
                                      related_name='photoaboardestate_aboard_estate_related')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Фото зарубежной недвижимости'
        verbose_name_plural = u'Фото зарубежной недвижимости'


class Country(models.Model):
    """
    Страны

    Поля:
    name - название страны
    """

    name = models.CharField(u'Наименование', max_length=250)

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Страна'
        verbose_name_plural = u'Страны'