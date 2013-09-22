# -*- coding:utf-8 -*-
from django.db import models
from new_building.models import Address
from commercial_estate.models import Communications
from common.models import PriceMixin, SystemMixin, PhotoMeta
from seo.models import SeoMetaTags


class VillageAddress(Address):
    """
    Адресс для загорода

    Поля:
    to_city - до города км
    """

    to_city = models.PositiveIntegerField(u'До города км')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Адрес для загорода'
        verbose_name_plural = u'Адреса для загорода'


class HomesteadObj(SeoMetaTags):
    """
    Родительская модель - Объект - Загородны участок

    Поля:
    address - адрес участка
    area - общая площадь
    use_to - назначение
    communicatons - коммуникации
    """
    
    address = models.ForeignKey('VillageAddress',
                                verbose_name=u'Адрес участка',
                                related_name='homestead_address_related')
    area = models.DecimalField(u'Общая площадь', max_digits=6, decimal_places=2)
    use_to = models.ForeignKey('UseTo', verbose_name=u'Назначение', related_name='homestead_use_to_related')
    communications = models.ForeignKey(Communications,
                                       verbose_name=u'Комуникации',
                                       related_name='homestead_communications_related')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Объект Загородный участок'
        verbose_name_plural = u'Объект Загородные участки'


class UseTo(models.Model):
    """
    Назначение загородного участка

    Поля:
    name - виды применения загородного участка
    """

    name = models.CharField(u'Наименование', max_length=250)

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Назначение участка'
        verbose_name_plural = u'Назначения участка'


class Homestead(HomesteadObj, PriceMixin, SystemMixin):
    """
    Загородные участки

    Поля:
    """

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Загородный участок'
        verbose_name_plural = u'Загородные участки'


class PhotoHomestead(PhotoMeta):
    """
    Фото загородных участков

    Поля:
    homestead - объект загородного участка
    """

    homestead = models.ForeignKey('Homestead',
                                  verbose_name=u'Загородный участок',
                                  related_name='photohomestead_homestead_related')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Фото загородного участка'
        verbose_name_plural = u'Фото загородного участка'



class HousesWithPlots(SeoMetaTags, PriceMixin, SystemMixin):
    """
    Дома с участками

    Поля:
    sale - продажа? или аренда
    homestead - участок
    floors - этажность
    """

    sale = models.BooleanField(u'Продажа? или аренда')
    homestead = models.ForeignKey('HomesteadObj',
                                  verbose_name=u'Учаток',
                                  related_name='houseswithplots_homestead_related')
    floors = models.PositiveSmallIntegerField(u'Этажей')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Дом с участком'
        verbose_name_plural = u'Дома с участками'


class PhotoHouseWithPlots(PhotoMeta):
    """
    Фото домов с участками

    Поля:
    house_with_plots - объект домов с участками
    """

    house_with_plots = models.ForeignKey('HousesWithPlots',
                                         verbose_name=u'Дом с участком',
                                         related_name='photohousewithplots_house_with_plots_related')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Фото дома с участком'
        verbose_name_plural = u'Фото довом с участками'

