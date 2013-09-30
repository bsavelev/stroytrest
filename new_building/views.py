from django.views.generic import TemplateView


class TestCardView(TemplateView):
    template_name = 'card.html'
