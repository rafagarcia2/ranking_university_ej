from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ranking_geral),
    url(r'^ranking_geral/$', views.ranking_geral, name='ranking_geral'),
    url(r'^ranking_cultura/$', views.ranking_cultura, name='ranking_cultura'),
    url(r'^ranking_inovacao/$', views.ranking_inovacao, name='ranking_inovacao'),
    url(r'^ranking_extensao/$', views.ranking_extensao, name='ranking_extensao'),
    url(r'^ranking_infraestrutura/$', views.ranking_infraestrutura, name='ranking_infraestrutura'),
    url(r'^ranking_internacionalizacao/$', views.ranking_internacionalizacao, name='ranking_internacionalizacao'),
    url(r'^ranking_capital/$', views.ranking_capital, name='ranking_capital'),
]