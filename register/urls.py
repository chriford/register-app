from django.urls import path
from .views import home_api_view, update_or_delete_api_view

urlpatterns = [
    path('', home_api_view, name='get'),
    path('<int:pk>/', update_or_delete_api_view),
]
