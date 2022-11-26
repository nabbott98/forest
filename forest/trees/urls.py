from django.urls import path 
from .views.tree_views import TreesView, TreeDetailView
from .views.park_views import ParksView, ParkDetailView

urlpatterns = [
    path('trees/', TreesView.as_view(), name='trees'),
    path('trees/<int:pk>/', TreeDetailView.as_view(), name='tree'),
    path('parks/', ParksView.as_view(), name='parks'),
    path('parks/<int:pk>/', ParkDetailView.as_view(), name='park'),
]