from django.urls import path
from . import views


# https://forum.codewithmosh.com/t/noreversematch-at-movies-is-not-a-registered-namespace/8466
app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.detail, name='detail')
]
