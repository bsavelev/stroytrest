# -*- coding:utf-8 -*-
__author__ = 'michael'
from django import forms

SEARCH_TYPE_CHOISE = (
    ('1', 'комплексам' ),
    ('2', 'квартирам'),
)

#TODO: Проверка каждого поля что такой объект в модели существует!!!

class NewBuildingForm(forms.Form):
    """
    Форма новостроект
    """
    price_from = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'price_from1'}))
    price_to = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'price_to1'}))
    credit = forms.BooleanField(required=False)
    ipoteka = forms.BooleanField(required=False)
    repair = forms.BooleanField(required=False)
    subsid = forms.BooleanField(required=False)
    house_type = forms.TypedChoiceField(choices=[('0', 'Тип дома'),('1','Тип номер 1'), ('2', 'Тип номер 2')],
                                        coerce=int,
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
    city = forms.TypedChoiceField(choices=(('0', 'Город'), ('1', 'Спб')), coerce=int, required=False)
    district = forms.TypedChoiceField(choices=(('0', 'Район'), ('1', 'Район номер 1'), ('2','Район номер 2')),
                                              coerce=int,
                                              required=False)
    region = forms.TypedChoiceField(choices=(('0', 'Населенный пункт'), ('1', 'Нас 1')), coerce=int, required=False)
    metro_stantions_list = forms.TypedMultipleChoiceField(choices=(('0', 'Девяткино'), ('1', 'Гражданский проспект')),
                                                  coerce=int,
                                                  required=False,
                                                  widget=forms.SelectMultiple(attrs={'class':'metro-stantions-list',
                                                                                     'style':'display:none;'}))
    search_type = forms.TypedChoiceField(widget=forms.RadioSelect(),
                                         choices=SEARCH_TYPE_CHOISE,
                                         coerce=int,
                                         required=False,
                                         initial=SEARCH_TYPE_CHOISE[0])


class ApartmentForm(forms.Form):
    """

    """

    price_from = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'price_from2'}))
    price_to = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'price_to2'}))
    credit = forms.BooleanField(required=False)
    ipoteka = forms.BooleanField(required=False)
    repair = forms.BooleanField(required=False)
    subsid = forms.BooleanField(required=False)
    house_type = forms.TypedChoiceField(choices=[('0', 'Тип дома'),('1','Тип номер 1'), ('2', 'Тип номер 2')],
                                        coerce=int,
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
    city = forms.TypedChoiceField(choices=(('0', 'Город'), ('1', 'Спб')), coerce=int, required=False)
    district = forms.TypedChoiceField(choices=(('0', 'Район'), ('1', 'Район номер 1'), ('2','Район номер 2')),
                                              coerce=int,
                                              required=False)
    region = forms.TypedChoiceField(choices=(('0', 'Населенный пункт'), ('1', 'Нас 1')), coerce=int, required=False)
    metro_stantions_list = forms.TypedMultipleChoiceField(choices=(('0', 'Девяткино'), ('1', 'Гражданский проспект')),
                                                  coerce=int,
                                                  required=False,
                                                  widget=forms.SelectMultiple(attrs={'class':'metro-stantions-list',
                                                                                     'style':'display:none;'}))
    sale_type = forms.TypedChoiceField(widget=forms.RadioSelect(),
                                       choices=(('1', 'Продажа'), ('2', 'Аренда')),
                                       required=False,
                                       coerce=int)


class RoomsForm(forms.Form):
    """

    """
    sale_type = forms.TypedChoiceField(widget=forms.RadioSelect(),
                                       choices=(('1', 'Продажа'), ('2', 'Аренда')),
                                       required=False,
                                       coerce=int)
    price_from = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'price_from3'}))
    price_to = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'price_to3'}))
    house_type = forms.TypedChoiceField(choices=[('0', 'Тип дома'),('1','Тип номер 1'), ('2', 'Тип номер 2')],
                                        coerce=int,
                                        required=False)
    floor_from = forms.IntegerField(required=False)
    floor_to = forms.IntegerField(required=False)
    studio = forms.BooleanField(required=False)
    room_value_1 = forms.BooleanField(required=False)
    room_value_2 = forms.BooleanField(required=False)
    all_room_value_2 = forms.BooleanField(required=False)
    all_room_value_3 = forms.BooleanField(required=False)
    all_room_value_4 = forms.BooleanField(required=False)
    area_from = forms.DecimalField(required=False)
    area_to = forms.DecimalField(required=False)
    city = forms.TypedChoiceField(choices=(('0', 'Город'), ('1', 'Спб')), coerce=int, required=False)
    district = forms.TypedChoiceField(choices=(('0', 'Район'), ('1', 'Район номер 1'), ('2','Район номер 2')),
                                              coerce=int,
                                              required=False)
    region = forms.TypedChoiceField(choices=(('0', 'Населенный пункт'), ('1', 'Нас 1')), coerce=int, required=False)
    metro_stantions_list = forms.TypedMultipleChoiceField(choices=(('0', 'Девяткино'), ('1', 'Гражданский проспект')),
                                                  coerce=int,
                                                  required=False,
                                                  widget=forms.SelectMultiple(attrs={'class':'metro-stantions-list',
                                                                                     'style':'display:none;'}))


class CommercialEstateForm(forms.Form):
    """

    """
    sale_type = forms.TypedChoiceField(widget=forms.RadioSelect(),
                                       choices=(('1', 'Продажа'), ('2', 'Аренда')),
                                       required=False,
                                       coerce=int)
    price_from = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'price_from4'}))
    price_to = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'price_to4'}))
    area_from = forms.DecimalField(required=False)
    area_to = forms.DecimalField(required=False)
    type_of_use = forms.TypedChoiceField(required=False,
                                         choices=(('0', 'Вид использования'), ('1', 'Вид исп 1')),
                                         coerce=int)
    city = forms.TypedChoiceField(choices=(('0', 'Город'), ('1', 'Спб')), coerce=int, required=False)
    district = forms.TypedChoiceField(choices=(('0', 'Район'), ('1', 'Район номер 1'), ('2','Район номер 2')),
                                              coerce=int,
                                              required=False)
    region = forms.TypedChoiceField(choices=(('0', 'Населенный пункт'), ('1', 'Нас 1')), coerce=int, required=False)
    metro_stantions_list = forms.TypedMultipleChoiceField(choices=(('0', 'Девяткино'), ('1', 'Гражданский проспект')),
                                                  coerce=int,
                                                  required=False,
                                                  widget=forms.SelectMultiple(attrs={'class':'metro-stantions-list',
                                                                                     'style':'display:none;'}))


class HousesForm(forms.Form):
    """

    """
    sale_type = forms.TypedChoiceField(widget=forms.RadioSelect(),
                                       choices=(('1', 'Продажа'), ('2', 'Аренда')),
                                       required=False,
                                       coerce=int)
    price_from = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'price_from5'}))
    price_to = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'price_to5'}))
    to_city_from = forms.DecimalField(required=False)
    to_city_to = forms.DecimalField(required=False)
    area_from = forms.DecimalField(required=False)
    area_to = forms.DecimalField(required=False)
    homestead_area_from = forms.DecimalField(required=False)
    homestead_area_to = forms.DecimalField(required=False)
    use_to = forms.TypedChoiceField(required=False,
                                    coerce=int,
                                    choices=(('0', 'Назначение участка'), ('1','Назн 1')))
    city = forms.TypedChoiceField(choices=(('0', 'Город'), ('1', 'Спб')), coerce=int, required=False)
    district = forms.TypedChoiceField(choices=(('0', 'Район'), ('1', 'Район номер 1'), ('2','Район номер 2')),
                                              coerce=int,
                                              required=False)
    region = forms.TypedChoiceField(choices=(('0', 'Населенный пункт'), ('1', 'Нас 1')), coerce=int, required=False)


class HomesteadForm(forms.Form):
    """

    """

    price_from = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'price_from6'}))
    price_to = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'price_to6'}))
    to_city_from = forms.DecimalField(required=False)
    to_city_to = forms.DecimalField(required=False)
    homestead_area_from = forms.DecimalField(required=False)
    homestead_area_to = forms.DecimalField(required=False)
    use_to = forms.TypedChoiceField(required=False,
                                    coerce=int,
                                    choices=(('0', 'Назначение участка'), ('1','Назн 1')))
    city = forms.TypedChoiceField(choices=(('0', 'Город'), ('1', 'Спб')), coerce=int, required=False)
    district = forms.TypedChoiceField(choices=(('0', 'Район'), ('1', 'Район номер 1'), ('2','Район номер 2')),
                                              coerce=int,
                                              required=False)
    region = forms.TypedChoiceField(choices=(('0', 'Населенный пункт'), ('1', 'Нас 1')), coerce=int, required=False)


class AboardEstateForm(forms.Form):
    """

    """

    sale_type = forms.TypedChoiceField(widget=forms.RadioSelect(),
                                       choices=(('1', 'Продажа'), ('2', 'Аренда')),
                                       required=False,
                                       coerce=int)
    price_from = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'price_from7'}))
    price_to = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'price_to7'}))
    country = forms.TypedChoiceField(required=False,
                                     coerce=int,
                                     choices=(('0', 'Страна'), ('1', 'Россия')))


class FastSearchForm(forms.Form):
    """

    """

    price_from = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'price_from'}))
    price_to = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'price_to'}))
    area_from = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'area_from'}))
    area_to = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'area_to'}))
    years_from = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'years_from'}))
    years_to = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'id':'years_to'}))


#TODO: сделать форму быстрого поиска, проверку формы