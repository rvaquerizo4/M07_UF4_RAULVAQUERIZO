from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('prof', views.profs, name='profs'),
    path('alumn', views.alumns, name='alumns'),
    path('prof/<str:pk>', views.prof, name='prof'),
    path('alumn/<str:pk>', views.alumn, name='alumn'),
    path('alumn/alum-form/', views.form_alum, name='form_alum'),
    path('prof/prof-form/', views.form_prof, name='form_prof'),
    path('alumn/update/<str:pk>/', views.update_alumn, name='update_alumn'),
    path('prof/update/<str:pk>/', views.update_prof, name='update_prof')
]