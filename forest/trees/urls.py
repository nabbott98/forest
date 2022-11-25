from django.urls import path 
from .views import TreesView, TreeDetailView

urlpatterns = [
    path('', TreesView.as_view(), name='trees'),
    path('<int:pk>/', TreeDetailView.as_view(), name='tree')
]