from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse


def book_detail_query_str(request):
    book_id = request.GET.get('id')
    name = request.GET.get('name')
    # name = request.GET['fuck'] 这种方式在属性不存在时会报错
    return HttpResponse(f"您查找的图书id是: {book_id}，图书名: {name}")


def book_detail_path(request, book_id):
    return HttpResponse(f"您查找的图书id是: {book_id}")


def book_slug(request, book_id):
    return HttpResponse(f"您找的图书id是: {book_id}")


def book_path(request, book_id):
    return HttpResponse(f"您找的图书id是: {book_id}")