# -*- coding:utf-8 -*-
__author__ = 'michael'
from django import forms


class NewBuildingForm(forms.Form):
    """
    Форма новостроект
    """
    price_from = forms.DecimalField()
    price_to = forms.DecimalField()
    credit = forms.BooleanField()
    ipoteka = forms.BooleanField()
    repair = forms.BooleanField()
    subsid = forms.BooleanField()
    house_type = forms.TypedChoiceField(choices=[('1','Тип номер 1'), ('2', 'Тип номер 2')],
                                        coerce=int,
                                        empty_value=u'Тип дома')
    floor_from = forms.IntegerField()
    floor_to = forms.IntegerField()
    studio = forms.BooleanField()
    room_value_1 = forms.BooleanField()
    room_value_2 = forms.BooleanField()
    room_value_3 = forms.BooleanField()
    room_value_4 = forms.BooleanField()
    area_from = forms.DecimalField()
    area_to = forms.DecimalField()
    kitchen_area_from = forms.DecimalField()
    kitchen_area_to = forms.DecimalField()
    district = forms.TypedChoiceField(choices=(('', 'Район выбрать'),('1', 'Район номер 1'), ('2','Район номер 2')),
                                              coerce=int,
                                              empty_value=u'Район')
    search_type = forms.TypedChoiceField(choices=(('1','Квартиры'), ('2','Комплексы')),
                                         coerce=int,
                                         widget=forms.RadioSelect)
