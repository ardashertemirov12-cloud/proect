from django.urls import path
from .views import shahar, viloyat, mamlakat, shahar_viloyat, shahar_viloyat_mamlakat, all_news, detail



urlpatterns = [
    path('shahar/', shahar),
    path('viloyat/', viloyat),
    path('mamlakat/', mamlakat),
    path('shahar/viloyat/', shahar_viloyat),
    path('shahar/viloyat/mamlakat/', shahar_viloyat_mamlakat),
    path('all_news/', all_news, name='news'),
    path('detail/<int:id>/',detail, name='detail' )
]














