from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('prof', views.profs, name='profs'),
    path('alumn', views.alumns, name='alumns'),
    path('prof/<str:pk>', views.prof, name='prof'),
    path('alumn/<str:pk>', views.alumn, name='alumn'),
]