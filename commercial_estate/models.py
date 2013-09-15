# -*- coding:utf-8 -*-
from django.db import models
from new_building.models import Building
from common.models import SystemMixin
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


class CommercialEstate(ApartmentObj, SystemMixin):
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
    communications = models.ForeignKey('Communications',
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
