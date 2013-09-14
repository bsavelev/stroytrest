from django.views.generic import TemplateView


class TestMainView(TemplateView):
    template_name = "index.html"


class TestListView(TemplateView):
    template_name = 'list.html'


class TestCardView(TemplateView):
    template_name = 'card.html'
