# -*- coding:utf-8 -*-
__author__ = 'michael'

from django.db import models
from django.contrib.auth.models import User, Group
from datetime import datetime
from django.conf import settings
from os.path import exists, join
from os import makedirs


class SystemMixin(object):
    """
    Микшин модель

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


class PriceMixin(object):
    """
    Микшин для цена

    Поля:
    price - цена чего либо
    """

    price = models.DecimalField(u'Цена', max_digits=9, decimal_places=2)


def get_or_create_dir(root_dir, dir_name):
    """
    Проверяет есть ли такая директория и создает ее если нету

    Логика:
    Возвращает Истину если такая директория есть или была создана удачно
    Возвращает Лож если такой директории нету и не удалоь ее создать

    Переменные:
    root_dir - путь к папке где будет находиться каталог
    dir_name - название котаога
    """
    full_dir = join(root_dir, dir_name)
    if not exists(full_dir):
        try:
            makedirs(full_dir)
        except OSError:
            return False
    return True


def get_upload_to_path(instance, filename, force_name=False, root_dir=settings.MEDIA_ROOT):
    """
    Функция для получения пути к сохранению файла

    Логика:
    Функция проверяет если ли папка и возвращает в зависимости от этого нужный урл

    Переменные:
    instance - инстанс класса
    filename - имя файла который пытаются загрузить
    force_name - имя директории указывается вручную
    root_dit - каталог в котором будет храниться диреткория
    """
    instance_dir = instance.__class__.name if not force_name else force_name
    if get_or_create_dir(root_dir, instance_dir):
        url = u'%s/%s_%s' % (instance_dir, datetime.now(), filename,)
    else:
        url = u'%s_%s' % (datetime.now(), filename,)
        #TODO: запись в лог
    return url


class PhotoMeta(models.Model):
    """
    Мета модель для фотографий

    Поля:
    photo - фотография
    """

    photo = models.ImageField(u'Фото', upload_to=get_upload_to_path)

    class Meta:
        abstract = True
