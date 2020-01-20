from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage),
    path('count/', views.count,name = 'count')
]
