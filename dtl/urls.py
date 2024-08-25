from django.urls import path

from . import views

app_name = "dtl"

urlpatterns = [
    path('', views.index, name='index'),
    path('info', views.info, name='info'),

    path('url', views.url_view, name='url_view'),

    path('filter', views.filter_view, name='filter'),

    path('home', views.template_form, name='template_form'),

    path('template/structure', views.template_structure, name='template_structure'),
]