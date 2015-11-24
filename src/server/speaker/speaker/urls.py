from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin



urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += i18n_patterns(
    url(r'^compass/', include('compass.urls')),
)

