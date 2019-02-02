from django.contrib import admin
from django.urls import path
from .views import contact, login_page, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact, name="contact"),
    path('login/', login_page, name="login"),
    path('register/', register_view, name="register")
]
