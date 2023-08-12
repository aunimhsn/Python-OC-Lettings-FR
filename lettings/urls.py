from django.urls import path
from . import views

# https://forum.codewithmosh.com/t/noreversematch-at-movies-is-not-a-registered-namespace/8466
app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.detail, name='detail')
]