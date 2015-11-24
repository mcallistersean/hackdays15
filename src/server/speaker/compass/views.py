from django.views.generic import DetailView, TemplateView


class LeafDetail(DetailView):
    template_name = 'compass/leaf.html'

class CompassStartView(TemplateView):
    template_name = 'compass/start.html'


