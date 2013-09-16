# -*- coding:utf-8 -*-
from django.db import models
from new_building.models import Building
from common.models import SystemMixin, PriceMixin, PhotoMeta
from apartment.models import ApartmentObj


class BuildingCommerce(Building, SystemMixin):
    """
    Комплекс для комерческой недвижимости

    Поля:
    наследуемые
    """

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Комплекс комерческой недвижимости'
        verbose_name_plural = u'Комплекс комерческой недвижимости'
        
        
class PhotoBildingCommerce(PhotoMeta):
    """
    Фото для коплекса комерческой недвижимости
    
    Поля:
    building_commerce - объект коплекс комерческой недвижимости
    """

    building_commerce = models.ForeignKey('BuildingCommerce', 
                                          verbose_name=u'Комплекс комерческой недвижимости', 
                                          related_name='photobuildingcommecrce_building_commerce_related')    

    def __unicode__(self):
        return u'%s' % (self.id,)
        
    class Meta:
        verbose_name = u'Фото комплекса ком. недвижимости'
        verbose_name_plural = u'Фото комплекса ком. недвижимости'



class CommercialEstate(ApartmentObj, SystemMixin, PriceMixin):
    """
    Комерческая недвижимость

    Поля:
    sale - продажа? или аренда
    type_of_use - вид использования
    communications - комуникации
    building - комплекс комерческой недвижимости
    """

    sale = models.BooleanField(u'Продажа? или аренад', default=True)
    type_of_use = models.ForeignKey('TypeOfUse',
                                    verbose_name=u'Вид использования',
                                    related_name='commecialestate_typeofuse_related')
    communications = models.ForeignKey('CommunicationsWithInternet',
                                       verbose_name=u'Комуникации',
                                       related_name='commercialestate_communications_related')
    building = models.ForeignKey('BuildingCommerce',
                                 verbose_name=u'Коплекс',
                                 related_name='commercialestate_building_related')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Комерческая недвижимость'
        verbose_name_plural = u'Комерческая недвижимость'
        
        
class PhotoCommercialEstate(PhotoMeta):
    """
    Фото комерческой недвижимости
    
    Поля:
    commercial_estate - объект комерческой недвижимости
    """
    
    commercial_estate = models.ForeignKey('CommercialEstate',
                                          verbose_name=u'Комерческая недвижимость',
                                          related_name='photocommercialestate_commercial_estate_related')

    def __unicode__(self):
        return u'%s' % (self.id,)
        
    class Meta:
        verbose_name = u'Фото комерческой недвижимости'
        verbose_name_plural = u'Фото комерческой недвижимости'



class TypeOfUse(models.Model):
    """
    Вид использования

    Поля:
    name - вид использования
    """

    name = models.CharField(u'Вид использования', max_length=250)

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Вид использования'
        verbose_name_plural = u'Виды использования'


class Communications(models.Model):
    """
    Коммуникации

    Поля:
    electricity - электричество
    water - вода
    heating - отопление
    gas - газ
    """

    electricity = models.ForeignKey('Electricity',
                                    verbose_name=u'Электричество',
                                    related_name='communications_electricity_related')
    water = models.ForeignKey('Water', verbose_name=u'Вода', related_name='communications_water_related')
    heating = models.ForeignKey('Heating', verbose_name=u'Отопление', related_name='communications_heating_related')
    gas = models.BooleanField(u'Газ')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Коммуникации'
        verbose_name_plural = u'Коммуникации'


class CommunicationsWithInternet(Communications):
    """
    Коммуникации с интернетом

    Поля:
    internet - наличие интернета
    """

    internet = models.BooleanField(u'Интернет')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Комуникации с интернетом'
        verbose_name_plural = u'Коммуникации с интернетом'


class Electricity(models.Model):
    """
    Электричество

    Поля:
    name - вид электричества
    """

    name = models.CharField(u'Наименование', max_length=250)

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Электричество'
        verbose_name_plural = u'Электричество'


class Water(models.Model):
    """
    Вода

    Поля:
    name - вид водяной комуникации
    """

    name = models.CharField(u'Наименование', max_length=250)

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Вода'
        verbose_name_plural = u'Вода'


class Heating(models.Model):
    """
    Отопление

    Поля:
    name - вид отопления
    """

    name = models.CharField(u'Наименование', max_length=250)

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Отопление'
        verbose_name_plural = u'Отопление'



#TODO: сделать admin.py


