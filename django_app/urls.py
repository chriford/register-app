# Main URL FILE
from os import name
from django.contrib import admin
from django.urls import path, include
from register.views import (
    index_view, signup_view, update_or_delete_view,
    register_view, admin_view, login_view
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('register.urls')),
    path('', index_view, name='index'),
    path('delete/update/<int:pk>/', update_or_delete_view, name='delup'),
    path('register/', register_view, name="register"),
    path('user/admin/page/', admin_view, name="admin"),
    path('signup/', signup_view, name="signup"),
    path('login/', login_view, name="login")
]
