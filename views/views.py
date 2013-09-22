# -*- coding:utf-8 -*-
__author__ = 'michael'
from django.views.generic import TemplateView
from static_values.models import StaticValues
from slider.models import Slider


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



from django.views.generic.base import ContextMixin
class TestFormView(TemplateView, ContextMixin):
    """
    Для тестирования форм
    """
    template_name = 'form-test.html'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates a blank version of the form.
        """
        form_class1 = self.get_form1_class()
        form1 = self.get_form(form_class1)
        form_class2 = self.get_form2_class()
        form2 = self.get_form(form_class2)
        return self.render_to_response(self.get_context_data(form1=form1, form2=form2))

    def get_form1_class(self):
        """
        получение класса первой формы
        """
        from forms.forms import NewBuildingForm
        form_class = NewBuildingForm
        return form_class


    def get_form2_class(self):
        """
        получение класса первой формы
        """
        from forms.forms import NewBuildingForm
        form_class = NewBuildingForm
        return form_class

    def get_form(self, form_class):
        """
        Returns an instance of the form to be used in this view.
        """
        return form_class(**self.get_form_kwargs())

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instantiating the form.
        """
        return {}

