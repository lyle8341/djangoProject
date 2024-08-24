"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, reverse
from book import views
from django.shortcuts import HttpResponse


def index(request):
    print(f'测试无参reverse: {reverse("book_detail_query_str")}')
    print(f'测试带参reverse: {reverse("book_detail_path", kwargs={"book_id": 123})}')
    return HttpResponse("Welcome to Django!")


urlpatterns = [
    path('', index, name="index"),
    path("admin/", admin.site.urls),
    path("book", views.book_detail_query_str, name="book_detail_query_str"),
    path("book/<int:book_id>", views.book_detail_path, name="book_detail_path"),

    path("book/slug/<slug:book_id>", views.book_slug, name="book_slug"),
    path("book/path/<path:book_id>", views.book_path),

    path('movie/', include("movie.urls")),  # movie ---> urls.py
]
