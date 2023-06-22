from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('destroy', views.destroy_session),
    path('two', views.up_two),
    path('custom', views.custom),
    path('custom_num', views.up_custom_num)
]