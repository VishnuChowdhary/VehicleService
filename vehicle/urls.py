from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name=''),
    path('customerclick', views.customerclick_view),
    path('mechanicsclick', views.mechanicsclick_view),
]