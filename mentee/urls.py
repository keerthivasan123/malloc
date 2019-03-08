from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.index, name='dashboard'),
    path('', views.register, name='index'),
    path('dashboard/connect/mentor/', views.my_view, name='map'),
    path('dashboard/connect', views.project, name='project'),
    path('dashboard/connect/rate', views.rate, name='rate'),
    path('dashboard/rating', views.rating1, name='rating'),
    
]

    