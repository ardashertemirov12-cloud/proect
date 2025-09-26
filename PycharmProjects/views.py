from django.shortcuts import render
from django.http import HttpResponse
from .models import Yangiliklar
from rest_framework import generics
from .serializers import YangiliklarSerializers


# Oddiy funksiyalar
def salom_beruvchi(request):
    return HttpResponse("Assalomu aleykum Ardasher Aka")

def alik_ol(request):
    return HttpResponse("Valeykum Asalom")

def shahar(request):
    return HttpResponse("Termez shahar")

def viloyat(request):
    return HttpResponse("Termez shahar, Surxandaryo viloyati")

def mamlakat(request):
    return HttpResponse("Termez shahar, Surxandaryo viloyati, O'zbekiston Respublikasi")

def shahar_viloyat(request):
    return HttpResponse("Termiz shahar, Surxandaryo viloyati")

def shahar_viloyat_mamlakat(request):
    return HttpResponse("Termiz shahar, Surxandaryo viloyati, O'zbekiston Respublikasi.")


# Yangiliklar - HTML sahifalar uchun
def all_news(request):
    news = Yangiliklar.objects.all()
    context = {
        'news': news
    }
    return render(request, 'all_news.html', context)

def detail(request, id):
    yangilik = Yangiliklar.objects.get(id=id)
    context = {
        'yangilik': yangilik
    }
    return render(request, 'detail.html', context)


# REST API uchun
class YangiliklarList(generics.ListCreateAPIView):
    queryset = Yangiliklar.objects.all()
    serializer_class = YangiliklarSerializers   # ✅ to‘g‘rilandi
