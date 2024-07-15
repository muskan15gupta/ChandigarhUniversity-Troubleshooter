# wardrobe/urls.py
from django.urls import path
from .views import (
    WardrobeItemListView,
    WardrobeItemDetailView,
    WardrobeItemCreateView,
    WardrobeItemUpdateView,
    WardrobeItemDeleteView,
    
)

app_name = 'wardrobe'

urlpatterns = [
    path('', WardrobeItemListView.as_view(), name='list'),
    path('<int:pk>/', WardrobeItemDetailView.as_view(), name='detail'),
    path('create/', WardrobeItemCreateView.as_view(), name='create'),
    path('update/<int:pk>/', WardrobeItemUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', WardrobeItemDeleteView.as_view(), name='delete'),
    
]
