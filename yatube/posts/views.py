from django.shortcuts import render

# Create your views here.
import django.http as http
def index(req):
    return http.HttpResponse('Главная страница Posts')

def group_posts(req):
    return http.HttpResponse("list of posts")