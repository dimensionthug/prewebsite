from django.urls import path
from . import views 



urlpatterns = [
    path('', views.homepage, name='home'),
    path('count/', views.count, name='count'),
    path('counting/', views.counting, name='counting'),
    path('fungames/', views.fungames, name='fungames'),
]
