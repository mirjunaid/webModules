from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.siteHome, name='siteHome'),
    path('calculator/', views.calculator, name='calculator'),
    path('weatherDetector/', views.weatherDetector, name='weatherDetector'),
    path('youtubeDownloader/', views.youtubeDownloader, name='youtubeDownloader'),
    path('calculator/smartCalc/<str:pk>', views.smartCalc, name='smartCalc'),
    path('results', views.volume, name='volume'),
]

