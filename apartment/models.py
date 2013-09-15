# -*- coding:utf-8 -*-
from django.db import models
from new_building.models import NewBuilding, Building
from common.models import SystemMixin
from new_building.models import Terms


class BuildingApertment(Building, SystemMixin):
    """
    Комплекс для квартир
    
    Поля:
    Наследуемые
    """

    def __unicode__(self):
        return u'%s' % (self.id,)
        
    class Meta:
        verbose_name = u''
        verbose_name_plural = u''



class ApartmentObj(models.Model):
    """
    Объект квартир

    Поля:
    number_of_rooms - количество комнат
    area - площадь квартиры
    toilet - сан. узел
    floor - этаж
    """

    number_of_rooms = models.ForeignKey('NumberOfRooms',
                                        verbose_name=u'Количество комнат',
                                        related_name='apartmentobj_numberofrooms_related')
    area = models.ForeignKey('Area', verbose_name=u'Площадь', related_name='apartmentobj_area_related')
    toilet = models.ForeignKey('Toilet', verbose_name=u'Сан.узел', related_name='apartmentobj_toilet_related')
    floor = models.PositiveSmallIntegerField(u'Этаж')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Объект квартиры'
        verbose_name_plural = u'Объекты квартиры'


class NumberOfRooms(models.Model):
    """
    Число комнат (студия, 1 комнатная, 2-х комнатная, 3-х комнатная и т.д.)

    Поля:
    name - число комнат или студия
    """

    name = models.CharField(u'Наименование', max_length=50)


    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Количество комнат'
        verbose_name_plural = u'Количество комнат'


class Area(models.Model):
    """
    Площадь комнаты

    Поля:
    gross_area - общая площадь
    kitchen_area - площадь кухни
    living_area - жилая площадь
    rooms_area - площадь комнат, текстом описание
    """

    gross_area = models.DecimalField(u'Общая площадь', max_digits=6, decimal_places=2)
    kitchen_area = models.DecimalField(u'Площадь кухни', max_digits=6, decimal_places=2)
    living_area = models.DecimalField(u'Жилая площадь', max_digits=6, decimal_places=2)
    rooms_area = models.CharField(u'Площадь комнат', max_length=200) 

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Площадь комнаты'
        verbose_name_plural = u'Площадь комнат'
        
        
class Toilet(models.Model):
    """
    Сан. узел
    
    Поля:
    name - вид сан.узла
    """
    
    name = models.CharField(u'Наименование', max_length=200)

    def __unicode__(self):
        return u'%s' % (self.id,)
        
    class Meta:
        verbose_name = u'Сан.узел'
        verbose_name_plural = u'Сан.узел'
        
        
class NewApartment(ApartmentObj, SystemMixin):
    """
    Квартира в новостройках
    
    Поля:
    building - комплекс новостроек
    price - цена квартиры 
    """

    building = models.ForeignKey(NewBuilding, verbose_name=u'Комплекс', related_name='newapartment_building_related')
    price = models.DecimalField(u'Цена', max_digits=9, decimal_places=0)

    def __unicode__(self):
        return u'%s' % (self.id,)
        
    class Meta:
        verbose_name = u'Квартира в новостройках'
        verbose_name_plural = u'Квартиры в вновостройках'
        
        
class ApartmentSecondary(ApartmentObj, SystemMixin):
    """
    Вторичное жилье, вартиры
    
    Поля:
    building - комплекс вторичного жилья
    sale - продажа? или аренда
    terms - условия
    price - цена
    """

    building = models.ForeignKey(BuildingApertment,
                                 verbose_name=u'Комплекс',
                                 related_name='apartmentsecondary_building_related')
    sale = models.BooleanField(u'Продажа? или аренда', default=True)
    terms = models.ForeignKey(Terms, verbose_name=u'Условия', related_name='apartmentsecondary_terms_related')
    price = models.DecimalField(u'Цена', max_digits=9, decimal_places=0)

    def __unicode__(self):
        return u'%s' % (self.id,)
        
    class Meta:
        verbose_name = u'Вторичная квартира'
        verbose_name_plural = u'Вторичные квартиры'


class RoomsSecondary(ApartmentObj, SystemMixin):
    """
    Вторичные комнаты

    Поля:
    building - комплекс вторичного жилья
    sale - продажа? или аренда
    rooms_numbers - количество комнат на продажу, аренду
    price - цена
    """

    building = models.ForeignKey(BuildingApertment,
                                 verbose_name=u'Комплекс',
                                 related_name='apartmentsecondary_building_related')
    sale = models.BooleanField(u'Продажа? или аренда', default=True)
    rooms_numbers = models.PositiveSmallIntegerField(u'Количество комнат на продажу/аренду')
    price = models.DecimalField(u'Цена', max_digits=9, decimal_places=0)

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Вторичная комната'
        verbose_name_plural = u'Вторичные комнаты'


#TODO: - сделать фотографии пропущенные




