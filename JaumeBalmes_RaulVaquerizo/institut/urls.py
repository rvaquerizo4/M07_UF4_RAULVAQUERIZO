from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prof', views.prof, name='prof'),
    path('alumn', views.alumn, name='alumn'),
]