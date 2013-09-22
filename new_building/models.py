# -*- coding:utf-8 -*-
from django.db import models
from common.models import SystemMixin, PhotoMeta
from seo.models import SeoMetaTags


class Building(SeoMetaTags):
    """
    Родительская модель для сданий, строений

    Поля:
    home_type - тип дома
    address - адрес дома
    floors - этажность, сколько этажей
    lift - присутствие лифта
    """

    home_type = models.ForeignKey('HomeType', verbose_name=u'Тип дома', related_name='building_home_type_related')
    address = models.ForeignKey('AddressWithMetro', verbose_name=u'Адрес', related_name='building_address_related')
    floors = models.PositiveSmallIntegerField(u'Этажность')
    lift = models.BooleanField(u'Присутствие лифта', default=True)

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Строения'
        verbose_name_plural = u'Строения'


class HomeType(models.Model):
    """
    Тип дома

    Поля:
    name - наименование
    """

    name = models.CharField(u'Наименование', max_length=100)

    def __unicode__(self):
        return u'%s' % (self.name, )

    class Meta:
        verbose_name = u'Тип дома'
        verbose_name_plural = u'Типы домов'
        ordering = ['name']


class City(models.Model):
    """
    Города

    Поля:
    name - наименование
    """

    name = models.CharField(u'Наименование', max_length=150)

    def __unicode__(self):
        return u'%s' % (self.name,)

    class Meta:
        verbose_name = u'Город'
        verbose_name_plural = u'Города'
        ordering = ['name']


class Region(models.Model):
    """
    Регион

    Поля:
    name - название региона
    """

    name = models.CharField(u'Наименование', max_length=150)

    def __unicode__(self):
        return u'%s' % (self.name,)

    class Meta:
        verbose_name = u'Регион'
        verbose_name_plural = u'Регионы'


class Locality(models.Model):
    """
    Населенный пункт

    Поля:
    name - название населенного пункта
    """

    name = models.CharField(u'Наименование', max_length=150)

    def __unicode__(self):
        return u'%s' % (self.name,)

    class Meta:
        verbose_name = u'Населенный пункт'
        verbose_name_plural = u'Населенные пункты'
        ordering = ['name']


class Streets(models.Model):
    """
    Улицы

    Поля:
    name - название улицы
    """

    name = models.CharField(u'Наименование', max_length=150)

    def __unicode__(self):
        return u'%s' % (self.name,)

    class Meta:
        verbose_name = u'Улица'
        verbose_name_plural = u'Улицы'
        ordering = ['name']


class Address(models.Model):
    """
    Адрес

    Поля:
    city - город
    region - район
    locality - населенный пункт
    street - улица
    house - дом
    """

    city = models.ForeignKey('City', verbose_name=u'Город', related_name='address_city_related')
    region = models.ForeignKey('Region', verbose_name=u'Регион', related_name='address_region_related')
    locality = models.ForeignKey('Locality', verbose_name=u'Населенный пункт', related_name='address_locality_related')
    street = models.ForeignKey('Streets', verbose_name=u'Улица', related_name='address_street_related')
    house = models.CharField(u'Дом', max_length=50)

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Адрес'
        verbose_name_plural = u'Адреса'


class AddressWithMetro(Address):
    """
    Адрес с метро

    Поля:
    metro - станция метро
    to_metro - минут до метро
    """

    metro = models.ForeignKey('Metro', verbose_name=u'Станция метро', related_name='addressWithMetro_metro_relared')
    to_metro = models.PositiveSmallIntegerField(u'Минут до метро')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Адрес с метро'
        verbose_name_plural = u'Адреса с метро'


class Metro(models.Model):
    """
    Метро

    Поля:
    name - название станции метро
    city - город где находиться метро
    """

    name = models.CharField(u'Наименование', max_length=100)
    city = models.ForeignKey('City', verbose_name=u'Город', related_name='metro_city_related')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Станция метро'
        verbose_name_plural = u'Станции метро'


class NewBuilding(Building, SystemMixin):
    """
    Сдание новостройки

    Поля:
    contract - договор
    terms - условия
    readiness - готовность
    developer - застройщик
    apartment_price - цена квартиры
    name - наименование
    completion - срок окончания страительства
    queue - очередь
    facing - отделка
    discounts - скидки
    activity_on_homepage - активность на главной странице
    """

    contract = models.ForeignKey('Contracts', verbose_name=u'Договор', related_name='newBuilding_contract_related')
    terms = models.ForeignKey('Terms', verbose_name=u'Условия', related_name='newBuilding_terms_related')
    readiness = models.ForeignKey('Readiness', verbose_name=u'Готовность', related_name='newBuilding_readiness_related')
    developer = models.ForeignKey('Developer', verbose_name=u'Застройщик', related_name='newBuilding_developer_related')
    apartment_price = models.ForeignKey('ApartmentPrice',
                                        verbose_name=u'Цена квартиры',
                                        related_name='newBuilding_apartment_price_related')
    name = models.CharField(u'Наименование', max_length=250)
    completion = models.DateField(u'Окончание строительства')
    queue = models.PositiveSmallIntegerField(u'Очередь')
    facing = models.BooleanField(u'Отделка')
    discounts = models.TextField(u'Скидки')
    activity_on_homepage = models.BooleanField(u'Активность на главной странице')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Новостройка'
        verbose_name_plural = u'Новостройки'


class PhotoNewBuilding(PhotoMeta):
    """
    Фото комплекса новостроек

    Поля:
    new_building - объект комплекса новостроек
    """

    new_building = models.ForeignKey('NewBuilding',
                                     verbose_name=u'Комплекс новостроек',
                                     related_name='photonewbuilding_new_building_related')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Фото комплекса новостроек'
        verbose_name_plural = u'Фото комплекса новостроек'



class Contracts(models.Model):
    """
    Договора на новостройки

    Поля:
    name - название договора
    """

    name = models.CharField(u'Наименование', max_length=50)

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Договор'
        verbose_name_plural = u'Договора'


class Terms(models.Model):
    """
    Условия новостроек

    Поля:
    mortgage - ипотека
    subsidies - субсидии
    installment_plan - рассрочка
    terms_of_payment - условия рассрочки
    installments_up_to - рассрочка до
    min_payment - минимальный взнос %
    manner_of_payment - порядок оплаты
    booking_conditions - условия бронирования
    """

    mortgage = models.BooleanField(u'Ипотека')
    subsidies = models.BooleanField(u'Субсидии')
    installment_plan = models.BooleanField(u'Расрочка')
    terms_of_payment = models.TextField(u'Условия рассрочки')
    installments_up_to = models.DateField(u'Рассрочка до')
    min_payment = models.PositiveSmallIntegerField(u'Минимальный взнос в %')
    manner_of_payment = models.TextField(u'Порядок оплаты')
    booking_conditions = models.TextField(u'Условия бронирования')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Условия новостройки'
        verbose_name_plural = u'Условия новостройки'


class Readiness(models.Model):
    """
    Готовность

    Поля:
    name - наименование готовности
    """

    name = models.CharField(u'Наименование', max_length=150)

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Готовность'
        verbose_name_plural = u'Готовность'


class Developer(models.Model):
    """
    Застройщик

    Поля:
    name - название застройщика
    address - адресс застройщика
    contacts - контакты застройщика
    """

    name = models.CharField(u'Наименование', max_length=150)
    address = models.ForeignKey('Address', verbose_name=u'Адрес', related_name='developer_address_related')
    contacts = models.TextField(u'Контакты')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Застройщик'
        verbose_name_plural = u'Застройщики'


class ApartmentPrice(models.Model):
    """
    Цена квартир в комплексе новостроек

    Поля:
    studio_price - цена студии
    studio_price_per_meter - цена за метр квадратный в студии
    one_bedroom_price - цена однокомнатной квартиры
    one_bedroom_price_per_meter - цена за метр однокомнатной квартиры
    two_bedroom_price - цена двухкомнатной квартиры
    two_bedroom_price_per_meter - цена за метр квадратный двухкомнатной квартиры
    three_bedroom_price - цена трехкомнатной квартиры
    three_bedroom_price_per_meter - цена за метр квадратный трехкомнатной квартиры
    """

    studio_price = models.DecimalField(u'Цена студии', max_digits=9, decimal_places=0)
    studio_price_per_meter = models.DecimalField(u'Цена метра студии', max_digits=9, decimal_places=0)
    one_bedroom_price = models.DecimalField(u'Цена однокомнатной', max_digits=9, decimal_places=0)
    one_bedroom_price_per_meter = models.DecimalField(u'Цена метра однокомнатной', max_digits=9, decimal_places=0)
    two_bedroom_price = models.DecimalField(u'Цена двухкомнатной', max_digits=9, decimal_places=0)
    two_bedroom_price_per_meter = models.DecimalField(u'Цена метра двухкомнатной', max_digits=9, decimal_places=0)
    three_bedroom_price = models.DecimalField(u'Цена трехкомнатной', max_digits=9, decimal_places=0)
    three_bedroom_price_per_meter = models.DecimalField(u'Цена метра трехкомнатной', max_digits=9, decimal_places=0)

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Цена квартиры'
        verbose_name_plural = u'Цены квартир'


#TODO: - Добавить историю к изменению комплексов новостроект, застройщикам, цены квартир, условиям
#TODO: (адрес и адрес с метро?)
#TODO: - сделать фотографии пропущнные