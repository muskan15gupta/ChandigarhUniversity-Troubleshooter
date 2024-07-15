from django.urls import path
from .views import outfit_recommendation_view  # Ensure correct import

app_name = 'recommendation'

urlpatterns = [
    path('', outfit_recommendation_view, name='outfit_recommendation'),  # Define URL for recommendation
]
