# -*- coding:utf-8 -*-
__author__ = 'michael'
from django.views.generic.base import ContextMixin
from django.utils.encoding import force_text
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404
from new_building.models import NewBuilding
from apartment.models import NewApartment, ApartmentSecondary, RoomsSecondary
from commercial_estate.models import CommercialEstate
from village.models import HousesWithPlots, Homestead
from aboard_estate.models import AboardEstate


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
    #TODO: дописать переменные

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
    form_submit_param = 'form_name'
    required_form_prefix = None
    new_building = None
    new_apartment = None
    apartment = None
    rooms_secondary = None
    commercial = None
    houses = None
    homestead = None
    aboard = None

    def render_all_forms(self, form=None, **kwargs):
        """

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
        if form:
            if form.prefix not in forms_dict.keys():
                    self.get_raise_404()
            forms_dict[form.prefix] = form
        context = self.get_context_data(**kwargs)
        context.update({
            'form_1':forms_dict[self.form_1_prefix],
            'form_2':forms_dict[self.form_2_prefix],
            'form_3':forms_dict[self.form_3_prefix],
            'form_4':forms_dict[self.form_4_prefix],
            'form_5':forms_dict[self.form_5_prefix],
            'form_6':forms_dict[self.form_6_prefix],
            'form_7':forms_dict[self.form_7_prefix],
            'form_8':forms_dict[self.form_8_prefix],
        })
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        """
        Обработка метода get запроса

        Переменные:
        request - сам запрос
        """
        return self.check_form(request, *args, **kwargs)

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
        kwargs.update({
            'data': self.request.GET,
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

    def form_valid(self, form, **kwargs):
        """
        Действия после успешной валидации формы
        """
        self.get_form_processing(form)
        return self.render_all_forms(form=form, **kwargs)

    def get_form_1_query(self, form):
        """

        """
        search_type = form.cleaned_data['search_type']
        if search_type == 1:
            #TODO: сделать выбор из списка заранее
            #query = NewBuilding.objects.all()
            #if price_from:
            #    query = query.filter(apartment_price__studio_price__gte=price_from)
            #if price_to:
            #    query = query.filter(apartment_price__three_bedroom_price__lte=price_to)
            #if credit:
            #    query = query.filter(terms__installment_plan=True)
            #if ipoteka:
            #    query = query.filter(terms__mortgage=True)
            #if repair:
            #    query = query.filter(facing=True)
            #if subsid:
            #    query = query.filter(subsidies=True)
            #if house_type:
            #    query = query.filter(home_type.id=house_type)
            self.new_building = self.get_query_building(form)
        elif search_type == 2:
            self.new_apartment = self.get_query_apartment(form)
        else:
            self.new_apartment = self.get_query_apartment(form)

    def get_query_apartment(self, form):
        """

        """
        query = NewApartment.objects.all()
        return query

    def get_query_building(self, form):
        """

        """
        query = NewBuilding.objects.all()
        return query

    def get_form_2_query(self, form):
        """

        """
        self.apartment = self.get_query_secondary_apartment(form)

    def get_query_secondary_apartment(self, form):
        query = ApartmentSecondary.objects.all()
        return query

    def get_form_3_query(self, form):
        """

        """
        self.rooms_secondary = self.get_query_rooms_secondary(form)

    def get_query_rooms_secondary(self, form):
        query = RoomsSecondary.objects.all()
        return query

    def get_form_4_query(self, form):
        """

        """
        self.commercial = self.get_query_commercial(form)

    def get_query_commercial(self, form):
        query = CommercialEstate.objects.all()
        return query

    def get_form_5_query(self, form):
        """

        """
        self.houses = self.get_query_houses(form)

    def get_query_houses(self, form):
        query = HousesWithPlots.objects.all()
        return query

    def get_form_6_query(self, form):
        """

        """
        self.homestead = self.get_query_homestead(form)

    def get_query_homestead(self, form):
        query = Homestead.objects.all()
        return query

    def get_form_7_query(self, form):
        """

        """
        self.aboard = self.get_query_aboard(form)

    def get_query_aboard(self, form):
        query = AboardEstate.objects.all()
        return query

    def get_form_8_query(self, form):
        """

        """
        self.new_apartment = self.get_query_fast_search_new_apartment(form)

    def get_query_fast_search_new_apartment(self, form):
        query = NewApartment.objects.all()
        return query

    def form_invalid(self, form, **kwargs):
        """
        Действия после провала валидации формы

        Переменные:
        form - передается форма, в корорую вводились данные для проверки
        """
        return self.render_all_forms(form=form, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Обработка post метода запроса

        Логика:
        Проверяем параметр get в котрый передается префикс формы, по нему вычисляется форма и проверяется на валидность
        """
        return self.render_all_forms(**kwargs)

    def check_form(self, request, *args, **kwargs):
        """
        """
        form_prefix = request.GET.get(self.form_submit_param, None)
        if not form_prefix:
            return self.render_all_forms(**kwargs)
        form_method = u'get_%s_class' % (form_prefix,)
        form_class = getattr(self, form_method, self.get_raise_404)
        form = self.get_form(form_class(), form_prefix)
        self.required_form_prefix = form_prefix
        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

    def get_raise_404(self, *args, **kwargs):
        """
        Вызывает сообщение 404 ошибки
        """
        raise Http404

    # PUT is a valid HTTP verb for creating (with a known URL) or editing an
    # object, note that browsers only support POST for now.
    def put(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_form_processing(self, form):
        """

        """
        if self.required_form_prefix is None:
            self.get_raise_404()
        method_name = u'get_%s_query' % (self.required_form_prefix,)
        form_query = getattr(self, method_name, self.get_raise_404)
        return form_query(form)
