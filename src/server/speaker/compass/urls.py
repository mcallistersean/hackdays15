from django.conf.urls import url, include
from .views import LeafDetail, CompassStartView
from .views import CompassPageList, CompassAddPage, QuestionnairePage, QuestionnaireCompleted

admin_urls = [
    url('^$', CompassPageList.as_view(), name='compass_admin_list'),
    url('^add/$', CompassAddPage.as_view(), name='compass_add_page'),
]


questionnaire_urls = [
    url(r'^$', QuestionnairePage.as_view(), name='questionnaire_start'),
    url(r'^(?P<step>\d)', QuestionnairePage.as_view(), name='questionnaire_step'),
    url(r'^completed/$', QuestionnaireCompleted.as_view(), name='questionnaire_completed')
]

urlpatterns = [
    url(r'^$', CompassStartView.as_view(), name='compass_start'),
    url(r'^(?P<pk>)/$', LeafDetail.as_view(), name='compass_leaf'),
    url(r'^q/', include(questionnaire_urls))
]

urlpatterns += [
    url(r'^admin/', include(admin_urls))
]
