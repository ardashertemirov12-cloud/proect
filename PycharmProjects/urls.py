from django.urls import path
from .views import (
    shahar, viloyat, mamlakat, shahar_viloyat, shahar_viloyat_mamlakat,
    all_news, detail, YangiliklarList
)

urlpatterns = [
    # REST API endpoint
    path('yangiliklar_list/', YangiliklarList.as_view(), name='yangiliklar_list'),

    # Oddiy funksiyalar
    path('shahar/', shahar, name='shahar'),
    path('viloyat/', viloyat, name='viloyat'),
    path('mamlakat/', mamlakat, name='mamlakat'),
    path('shahar-viloyat/', shahar_viloyat, name='shahar_viloyat'),
    path('shahar-viloyat-mamlakat/', shahar_viloyat_mamlakat, name='shahar_viloyat_mamlakat'),

    # HTML sahifalar
    path('all_news/', all_news, name='all_news'),
    path('detail/<int:id>/', detail, name='detail'),
]
