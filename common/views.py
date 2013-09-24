# -*- coding:utf-8 -*-
__author__ = 'michael'
from django.views.generic.base import ContextMixin
from django.utils.encoding import force_text
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect, Http404


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
    form_submit_param - параметр get запроса, в который передается префикс формы
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
    form_submit_param = 'p'

    def get(self, request, *args, **kwargs):
        """
        Обработка метода get запроса

        Переменные:
        request - сам запрос
        """
        form_class_1 = self.get_form_1_class()
        form_1 = self.get_form(form_class_1, prefix=self.form_1_prefix)
        form_class_2 = self.get_form_2_class()
        form_2 = self.get_form(form_class_2, prefix=self.form_2_prefix)
        return self.render_to_response(self.get_context_data(form_1=form_1, form_2=form_2))

    def get_form_1_class(self, *args, **kwargs):
        """
        Получение класса формы
        """
        return self.form_class_1

    def get_form_2_class(self, *args, **kwargs):
        """
        Получение класса формы
        """
        return self.form_class_2

    def get_form_3_class(self, *args, **kwargs):
        """
        Получение класса формы
        """
        return self.form_class_3

    def get_form_4_class(self, *args, **kwargs):
        """
        Получение класса формы
        """
        return self.form_class_4

    def get_form_5_class(self, *args, **kwargs):
        """
        Получение класса формы
        """
        return self.form_class_5

    def get_form_6_class(self, *args, **kwargs):
        """
        Получение класса формы
        """
        return self.form_class_6

    def get_form_7_class(self, *args, **kwargs):
        """
        Получение класса формы
        """
        return self.form_class_7

    def get_form_8_class(self, *args, **kwargs):
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

    def form_valid(self, form):
        """
        Действия после успешной валидации формы
        """
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """
        Действия после провала валидации формы

        Переменные:
        form - передается форма, в корорую вводились данные для проверки
        """
        forms_dict = {
            self.form_1_prefix: self.get_form(self.get_form_1_class(), prefix=self.form_1_prefix),
            self.form_2_prefix: self.get_form(self.get_form_2_class(), prefix=self.form_2_prefix),
            self.form_3_prefix: self.get_form(self.get_form_3_class(), prefix=self.form_3_prefix),
            self.form_4_prefix: self.get_form(self.get_form_4_class(), prefix=self.form_4_prefix),
            self.form_5_prefix: self.get_form(self.get_form_5_class(), prefix=self.form_5_prefix),
            self.form_6_prefix: self.get_form(self.get_form_6_class(), prefix=self.form_6_prefix),
            self.form_7_prefix: self.get_form(self.get_form_7_class(), prefix=self.form_7_prefix),
            self.form_8_prefix: self.get_form(self.get_form_8_class(), prefix=self.form_8_prefix),
        }
        if form.prefix not in forms_dict.keys():
            self.get_raise_404()
        forms_dict[form.prefix] = form
        return self.render_to_response(self.get_context_data(form_1=forms_dict[self.form_1_prefix],
                                                             form_2=forms_dict[self.form_2_prefix],
                                                             form_3=forms_dict[self.form_3_prefix],
                                                             form_4=forms_dict[self.form_4_prefix],
                                                             form_5=forms_dict[self.form_5_prefix],
                                                             form_6=forms_dict[self.form_6_prefix],
                                                             form_7=forms_dict[self.form_7_prefix],
                                                             form_8=forms_dict[self.form_8_prefix]))

    # def get_form_field(self, form, form_prefix):
    #     """
    #     Получение поля формы с префиксом
    #
    #     Переменные:
    #     form - форма
    #     form_prefix - префикс формы, чтобы составить полное название поля
    #     """
    #     return u'%s-%s' % (form_prefix, form.fields.keys()[0],)

    # def post_1(self, request, *args, **kwargs):
    #     """
    #     Обработка post метода запроса
    #
    #     Логика:
    #     Проверяет на валидацию ту форму для которой пришли данные
    #     """
    #     form_class_1 = self.get_form_1_class()
    #     form_class_2 = self.get_form_2_class()
    #     form_class_3 = self.get_form_3_class()
    #     form_class_4 = self.get_form_4_class()
    #     form_class_5 = self.get_form_5_class()
    #     form_class_6 = self.get_form_6_class()
    #     form_class_7 = self.get_form_7_class()
    #     form_class_8 = self.get_form_8_class()
    #     form_1 = self.get_form(form_class_1, prefix=self.form_1_prefix)
    #     form_2 = self.get_form(form_class_2, prefix=self.form_2_prefix)
    #     form_3 = self.get_form(form_class_3, prefix=self.form_3_prefix)
    #     form_4 = self.get_form(form_class_4, prefix=self.form_4_prefix)
    #     form_5 = self.get_form(form_class_5, prefix=self.form_5_prefix)
    #     form_6 = self.get_form(form_class_6, prefix=self.form_6_prefix)
    #     form_7 = self.get_form(form_class_7, prefix=self.form_7_prefix)
    #     form_8 = self.get_form(form_class_8, prefix=self.form_8_prefix)
    #     form_1_field = self.get_form_field(form_1, self.form_1_prefix)
    #     form_2_field = self.get_form_field(form_2, self.form_2_prefix)
    #     form_3_field = self.get_form_field(form_3, self.form_3_prefix)
    #     form_4_field = self.get_form_field(form_4, self.form_4_prefix)
    #     form_5_field = self.get_form_field(form_5, self.form_5_prefix)
    #     form_6_field = self.get_form_field(form_6, self.form_6_prefix)
    #     form_7_field = self.get_form_field(form_7, self.form_7_prefix)
    #     form_8_field = self.get_form_field(form_8, self.form_8_prefix)
    #     if form_1_field in request.POST:
    #         form = form_1
    #     elif form_2_field in request.POST:
    #         form = form_2
    #     elif form_3_field in request.POST:
    #         form = form_3
    #     elif form_4_field in request.POST:
    #         form = form_4
    #     elif form_5_field in request.POST:
    #         form = form_5
    #     elif form_6_field in request.POST:
    #         form = form_6
    #     elif form_7_field in request.POST:
    #         form = form_7
    #     elif form_8_field in request.POST:
    #         form = form_8
    #     else:
    #         raise Http404
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form_1)

    def post(self, request, *args, **kwargs):
        """
        Обработка post метода запроса

        Логика:
        Проверяем параметр get в котрый передается префикс формы, по нему вычисляется форма и проверяется на валидность
        """
        form_prefix = request.GET.get(self.form_submit_param, None)
        if not form_prefix:
            self.get_raise_404()
        form_method = u'get_%s_class' % (form_prefix,)
        form_class = getattr(self, form_method, self.get_raise_404)
        form = self.get_form(form_class(), form_prefix)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_raise_404(self, *args, **kwargs):
        """
        Вызывает сообщение 404 ошибки
        """
        raise Http404

    # PUT is a valid HTTP verb for creating (with a known URL) or editing an
    # object, note that browsers only support POST for now.
    def put(self, *args, **kwargs):
        return self.post(*args, **kwargs)
