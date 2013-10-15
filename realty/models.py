# -*- coding:utf-8 -*-
from django.db import models

PROPERTY_NAME = {
    1: {'name': 'integer', 'function': int},
    2: {'name': 'text', 'function': str}
}

PROPERTY_NAME_CHOICES = [(k, v['name'])for k, v in PROPERTY_NAME]


class State(models.Model):
    "город, область"
    name = models.CharField(max_length=255)


class Metro():
    "станция метро"
    city = models.ForeignKey(State)
    name = models.CharField(max_length=255)


class District(models.Model):
    "район"
    city = models.ForeignKey(State)
    name = models.CharField(max_length=255)


class Developer(models.Model):
    "застройщик"
    name = models.CharField(max_length=255)


class DeveloperProject(models.Model):
    "проект застройщика"
    name = models.CharField(max_length=255)
    developer = models.ForeignKey(Developer)


class RealtyType(models.Model):
    "тип недвижимости: первичка, вторичка, котедж"
    name = models.CharField(max_length=255)


class RealtyStatus(models.Model):
    "статус недвижимости: сдан, собственность, III 2014,..."
    name = models.CharField(max_length=255)


class PropertyName(models.Model):
    "имя доп. свойств для недвижимости"
    name = models.CharField(max_length=255)
    ptype = models.IntegerField(choices=PROPERTY_NAME_CHOICES)


class Property(models.Model):
    name = models.ForeignKey(PropertyName)
    value = models.TextField()


class Realty(models.Model):
    "объект недвижимости"
    rtype = models.ForeignKey(RealtyType)
    district = models.ForeignKey(District)
    rstatus = models.ForeignKey(RealtyStatus)
    metro = models.ForeignKey(Metro, blank=True, null=True)
    developer = models.ForeignKey(Developer, blank=True, null=True)
    address = models.TextField()
    flour = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2)
    rproperty = models.ManyToManyField(Property)


class Photo(models.Model):
    realty = models.ForeignKey(Realty)
    image = models.ImageField()
