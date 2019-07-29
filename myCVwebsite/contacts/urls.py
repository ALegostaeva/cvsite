from django.urls import path, include
from .views import emailview, successview

urlpatterns = [
    # path('', views.index, name='index'),
    path('', emailview, name='email'),
    path('thanks/', successview, name='thanks'),
]
