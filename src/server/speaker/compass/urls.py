from django.conf.urls import url
from .views import LeafDetail, CompassStartView

urlpatterns = [
    url(r'^$', CompassStartView.as_view(), name='compass_start'),
    url(r'^(?P<pk>)/$', LeafDetail.as_view(), name='compass_leaf')
]
