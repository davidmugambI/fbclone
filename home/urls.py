from django.urls import path, re_path
from home.views import HomeView
from . import views

app_name = 'home'
urlpatterns = [
    #path('', views.home, name='home')
    path('', HomeView.as_view(), name='home'),
    re_path('connect/(?P<operation>.+)/(?P<pk>\d+)/', views.change_friends, name='change_friend')
]