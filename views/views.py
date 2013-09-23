# -*- coding:utf-8 -*-
__author__ = 'michael'
from django.views.generic import TemplateView
from static_values.models import StaticValues
from slider.models import Slider
from forms.forms import NewBuildingForm1, NewBuildingForm2
from common.views import Forms2Mixin


class MainView(TemplateView):
    """
    Главная страница
    """

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



class TestFormView(Forms2Mixin, TemplateView):
    """
    Для тестирования форм
    """

    template_name = 'form-test.html'
    success_url = '/test-form/'
    form_class_1 = NewBuildingForm1
    form_class_2 = NewBuildingForm1
    form_class_3 = NewBuildingForm1
    form_class_4 = NewBuildingForm1
    form_class_5 = NewBuildingForm1
    form_class_6 = NewBuildingForm1
    form_class_7 = NewBuildingForm1
    form_class_8 = NewBuildingForm1

