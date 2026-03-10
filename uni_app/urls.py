
from django.urls import path
from . import views




urlpatterns = [
    path('', views.userview, name='home'),
    path('search/',views.search_course,name='search_course'),

]