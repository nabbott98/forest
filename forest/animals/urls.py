from django.urls import path 
from .views import AnimalsView, AnimalDetailView

urlpatterns = [
    path('', AnimalsView.as_view(), name='animals'),
    path('<int:pk>/', AnimalDetailView.as_view(), name='animal')
]