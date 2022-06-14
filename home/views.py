from django.views.generic import TemplateView


class HomeView(TemplateView):
    """
    View to render homepage
    """
    template_name = 'home/index.html'
