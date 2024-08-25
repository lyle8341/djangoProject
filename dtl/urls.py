from django.urls import path

from . import views

from django.conf.urls.static import static
from django.conf import settings

app_name = "dtl"

urlpatterns = [
    path('', views.index, name='index'),
    path('info', views.info, name='info'),

    path('url', views.url_view, name='url_view'),

    path('filter', views.filter_view, name='filter'),

    path('home', views.template_form, name='template_form'),

    path('template/structure', views.template_structure, name='template_structure'),

    path('statView', views.static_view, name='static_view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)