# -*- coding:utf-8 -*-
__author__ = 'michael'
from django import forms


class NewBuildingForm1(forms.Form):
    """
    Форма новостроект
    """
    price_from = forms.DecimalField(required=False)
    price_to = forms.DecimalField(required=False)
    credit = forms.BooleanField(required=False)
    ipoteka = forms.BooleanField(required=False)
    repair = forms.BooleanField(required=False)
    subsid = forms.BooleanField(required=False)
    house_type = forms.TypedChoiceField(choices=[('1','Тип номер 1'), ('2', 'Тип номер 2')],
                                        coerce=int,
                                        empty_value=u'Тип дома',
                                        required=False)
    floor_from = forms.IntegerField(required=False)
    floor_to = forms.IntegerField(required=False)
    studio = forms.BooleanField(required=False)
    room_value_1 = forms.BooleanField(required=False)
    room_value_2 = forms.BooleanField(required=False)
    room_value_3 = forms.BooleanField(required=False)
    room_value_4 = forms.BooleanField(required=False)
    area_from = forms.DecimalField(required=False)
    area_to = forms.DecimalField(required=False)
    kitchen_area_from = forms.DecimalField(required=False)
    kitchen_area_to = forms.DecimalField(required=False)
    district = forms.TypedChoiceField(choices=(('0', 'Район выбрать'),('1', 'Район номер 1'), ('2','Район номер 2')),
                                              coerce=int, required=False)
    search_type = forms.TypedChoiceField(choices=(('1','Квартиры'), ('2','Комплексы')),
                                         coerce=int,
                                         widget=forms.RadioSelect(attrs={'name': 'search11111111',}),
                                        required=False)


class NewBuildingForm2(forms.Form):
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
    district = forms.TypedChoiceField(choices=(('0', 'Район выбрать'),('1', 'Район номер 1'), ('2','Район номер 2')),
                                              coerce=int)
    search_type = forms.TypedChoiceField(choices=(('1','Квартиры'), ('2','Комплексы')),
                                         coerce=int,
                                         widget=forms.RadioSelect)
