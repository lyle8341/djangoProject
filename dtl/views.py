from django.shortcuts import render
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, "index.html")


def info(request):
    # 普通变量
    username = 'lyle'
    # 字典类型变量
    book = {'name': '三国演义', 'author': '罗贯中'}
    # 列表
    books = [
        {'name': '水浒传', 'author': '施耐庵'},
        {'name': '红楼梦', 'author': '曹雪芹'}
    ]
    # 对象
    class Person:
        def __init__(self, name):
            self.name = name


    context_param = {
        'username': username,
        'book': book,
        'books': books,
        'person': Person("公孙无知")
    }
    return render(request, "info.html", context=context_param)



def url_view(request):
    return render(request, "url.html")


def filter_view(request):
    greet = "hello world, hello django"
    context = {
        'greet': greet,
        'birthday': datetime.now(),
        'html': '<h1>这是一个富文本<h1>',
        'bigText':'this is a long long text'
    }
    return render(request, "filter.html",  context=context)



def template_form(request):
    context = {
        'articles': ['chatgpt10会思考了', '稳重向好']
    }
    return render(request,"home.html", context=context)


def template_structure(request):
    return render(request,"template_structure.html")


def static_view(request):
    return render(request, "static.html")
