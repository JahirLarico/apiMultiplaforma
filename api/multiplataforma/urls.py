from django.urls import path
from . import views

app_name = 'multiplataforma'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('recetas/', views.RecetasList.as_view()),
    path('recetas/<int:pk>/', views.RecetasDetail.as_view()),
    path('recetas/<str:name>/', views.RecetasDetailByName.as_view()),
    path('recetas/tipo/<str:tipo>/', views.RecetasDetailByTipo.as_view()),
]
