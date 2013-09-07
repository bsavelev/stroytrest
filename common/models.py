# -*- coding:utf-8 -*-
__author__ = 'michael'

from django.db import models
from django.contrib.auth.models import User, Group


class SystemMeta(models.Model):
    """
    Абстракная модель

    Поля:
    description - описание сущности, для общего отображения
    system_description - служебное описание сущности, для служебного пользования
    activity - активность
    owner - создатель
    owner_group - группу создателя
    created_date - дата создания
    """

    description = models.TextField(u'Описание')
    system_description = models.TextField(u'Служебное описание')
    activity = models.BooleanField(u'Активность', default = True)
    owner = models.ForeignKey(User, verbose_name=u'Создатель', related_name='%(app_label)s_%(class)s_related')
    owner_group = models.ForeignKey(Group,
                                    verbose_name=u'Группа создателя',
                                    related_name='%(app_label)s_%(class)s_related')
    created_date = models.DateTimeField(u'Дата создания')

    class Meta:
        abstract = True


class HistoryMeta(models.Model):
    """
    Абстрактная модель для истории и избранного

    Поля:
    username - пользователя, который произвел изменение
    change_date - дата изменения
    """

    username = models.ForeignKey(User,
                                 verbose_name=u'Изменивший пользователь',
                                 related_name='%(app_label)s_%(class)s_related')
    change_date = models.DateTimeField(u'Дата изменения')

    class Meta:
        abstract = True
