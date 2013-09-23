# -*- coding:utf-8 -*-
__author__ = 'michael'
from django.views.generic.base import ContextMixin
from django.utils.encoding import force_text
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect, Http404

#TODO: подумать как избавиться от повторений в формах

class Forms2Mixin(ContextMixin):
    """
    Микшин для 2 форм

    Логика:
    Миксуеться только с потомками класса TemplateView, ставить перед TemplateView в наследовании

    Обязательные переменные:
    form_class_1 - Класс формы №1
    form_class_2 - Класс формы №2
    form_class_3 - Класс формы №3
    form_class_4 - Класс формы №4
    form_class_5 - Класс формы №5
    form_class_6 - Класс формы №6
    form_class_7 - Класс формы №7
    form_class_8 - Класс формы №8
    initial - начальные данные формы - пока не задействованы
    form_1_prefix - префикс 1 формы для различия в шаблоне
    form_2_prefix - префикс 2 формы для различия в шаблоне
    form_3_prefix - префикс 3 формы для различия в шаблоне
    form_4_prefix - префикс 4 формы для различия в шаблоне
    form_5_prefix - префикс 5 формы для различия в шаблоне
    form_6_prefix - префикс 6 формы для различия в шаблоне
    form_7_prefix - префикс 7 формы для различия в шаблоне
    form_8_prefix - префикс 8 формы для различия в шаблоне
    success_url - урл успешно заполненной формы
    """

    initial = {}
    form_class_1 = None
    form_class_2 = None
    form_class_3 = None
    form_class_4 = None
    form_class_5 = None
    form_class_6 = None
    form_class_7 = None
    form_class_8 = None
    success_url = None
    form_1_prefix = 'form_1'
    form_2_prefix = 'form_2'
    form_3_prefix = 'form_3'
    form_4_prefix = 'form_4'
    form_5_prefix = 'form_5'
    form_6_prefix = 'form_6'
    form_7_prefix = 'form_7'
    form_8_prefix = 'form_8'


    def get(self, request, *args, **kwargs):
        """
        Обработка метода get запроса

        Переменные:
        request - сам запрос
        """
        form_class_1 = self.get_form_class_1()
        form_1 = self.get_form(form_class_1, prefix=self.form_1_prefix)
        form_class_2 = self.get_form_class_2()
        form_2 = self.get_form(form_class_2, prefix=self.form_2_prefix)
        return self.render_to_response(self.get_context_data(form_1=form_1, form_2=form_2))

    def get_form_class_1(self):
        """
        Получение класса формы
        """
        return self.form_class_1


    def get_form_class_2(self):
        """
        Получение класса формы
        """
        return self.form_class_2

    def get_form_class_3(self):
        """
        Получение класса формы
        """
        return self.form_class_3

    def get_form_class_4(self):
        """
        Получение класса формы
        """
        return self.form_class_4

    def get_form_class_5(self):
        """
        Получение класса формы
        """
        return self.form_class_5

    def get_form_class_6(self):
        """
        Получение класса формы
        """
        return self.form_class_6

    def get_form_class_7(self):
        """
        Получение класса формы
        """
        return self.form_class_7

    def get_form_class_8(self):
        """
        Получение класса формы
        """
        return self.form_class_8

    def get_form(self, form_class, prefix):
        """
        Получение формы
        """
        return form_class(prefix=prefix, **self.get_form_kwargs())

    def get_form_kwargs(self):
        """
        Получение переменных для формы из запроса
        """
        kwargs = {'initial': self.get_initial()}
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        return self.initial.copy()

    def get_success_url(self):
        """
        Returns the supplied success URL.
        """
        if self.success_url:
            # Forcing possible reverse_lazy evaluation
            url = force_text(self.success_url)
        else:
            raise ImproperlyConfigured(
                "No URL to redirect to. Provide a success_url.")
        return url

    def form_valid(self):
        """
        Действия после успешной валидации формы
        """
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form_1, form_2, form_3, form_4, form_5, form_6, form_7, form_8):
        """
        Действия после провала валидации формы
        """
        return self.render_to_response(self.get_context_data(form_1=form_1,
                                                             form_2=form_2,
                                                             form_3=form_3,
                                                             form_4=form_4,
                                                             form_5=form_5,
                                                             form_6=form_6,
                                                             form_7=form_7,
                                                             form_8=form_8))

    def get_form_field(self, form, form_prefix):
        """
        Получение поля формы с префиксом

        Переменные:
        form - форма
        form_prefix - префикс формы, чтобы составить полное название поля
        """
        return u'%s-%s' % (form_prefix, form.fields.keys()[0],)

    def post(self, request, *args, **kwargs):
        """
        Обработка post метода запроса

        Логика:
        Проверяет на валидацию ту форму для которой пришли данные
        """
        form_class_1 = self.get_form_class_1()
        form_class_2 = self.get_form_class_2()
        form_class_3 = self.get_form_class_3()
        form_class_4 = self.get_form_class_4()
        form_class_5 = self.get_form_class_5()
        form_class_6 = self.get_form_class_6()
        form_class_7 = self.get_form_class_7()
        form_class_8 = self.get_form_class_8()
        form_1 = self.get_form(form_class_1, prefix=self.form_1_prefix)
        form_2 = self.get_form(form_class_2, prefix=self.form_2_prefix)
        form_3 = self.get_form(form_class_3, prefix=self.form_3_prefix)
        form_4 = self.get_form(form_class_4, prefix=self.form_4_prefix)
        form_5 = self.get_form(form_class_5, prefix=self.form_5_prefix)
        form_6 = self.get_form(form_class_6, prefix=self.form_6_prefix)
        form_7 = self.get_form(form_class_7, prefix=self.form_7_prefix)
        form_8 = self.get_form(form_class_8, prefix=self.form_8_prefix)
        form_1_field = self.get_form_field(form_1, self.form_1_prefix)
        form_2_field = self.get_form_field(form_2, self.form_2_prefix)
        form_3_field = self.get_form_field(form_3, self.form_3_prefix)
        form_4_field = self.get_form_field(form_4, self.form_4_prefix)
        form_5_field = self.get_form_field(form_5, self.form_5_prefix)
        form_6_field = self.get_form_field(form_6, self.form_6_prefix)
        form_7_field = self.get_form_field(form_7, self.form_7_prefix)
        form_8_field = self.get_form_field(form_8, self.form_8_prefix)
        if form_1_field in request.POST:
            form = form_1
        elif form_2_field in request.POST:
            form = form_2
        elif form_3_field in request.POST:
            form = form_3
        elif form_4_field in request.POST:
            form = form_4
        elif form_5_field in request.POST:
            form = form_5
        elif form_6_field in request.POST:
            form = form_6
        elif form_7_field in request.POST:
            form = form_7
        elif form_8_field in request.POST:
            form = form_8
        else:
            raise Http404
        if form.is_valid():
            return self.form_valid()
        else:
            return self.form_invalid(form_1, form_2, form_3, form_4, form_5, form_6, form_7, form_8)

    # PUT is a valid HTTP verb for creating (with a known URL) or editing an
    # object, note that browsers only support POST for now.
    def put(self, *args, **kwargs):
        return self.post(*args, **kwargs)
