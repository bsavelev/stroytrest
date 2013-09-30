# -*- coding:utf-8 -*-
__author__ = 'michael'
from django.views.generic import TemplateView
from static_values.models import StaticValues
from slider.models import Slider
from forms.forms import NewBuildingForm, ApartmentForm, RoomsForm, CommercialEstateForm, HousesForm, HomesteadForm, \
    AboardEstateForm, FastSearchForm
from common.views import Forms2Mixin


class MainView(Forms2Mixin, TemplateView):
    """
    Главная страница
    """
    template_name = 'index.html'
    success_url = '/'
    form_class_1 = NewBuildingForm
    form_class_2 = ApartmentForm
    form_class_3 = RoomsForm
    form_class_4 = CommercialEstateForm
    form_class_5 = HousesForm
    form_class_6 = HomesteadForm
    form_class_7 = AboardEstateForm
    form_class_8 = FastSearchForm

    def get_static_values(self):
        """
        Получение статических данных

        адрес компании
        телефон компании
        часы работы компании
        логотип
        слоган
        """
        query = StaticValues.objects.all()[0]
        return query

    def get_sliders(self):
        """
        Получение активных слайдеров

        картинка
        ссылка
        """
        query = Slider.objects.filter(activity=True)
        return query


class ListFormView(Forms2Mixin, TemplateView):
    """

    """

    template_name = 'list.html'
    success_url = '/'
    form_class_1 = NewBuildingForm
    form_class_2 = ApartmentForm
    form_class_3 = RoomsForm
    form_class_4 = CommercialEstateForm
    form_class_5 = HousesForm
    form_class_6 = HomesteadForm
    form_class_7 = AboardEstateForm
    form_class_8 = FastSearchForm
