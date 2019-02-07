from django.contrib import admin
from django.urls import path, include
from .views import contact, login_page, register_view, home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact, name="contact"),
    path('login/', login_page, name="login"),
    path('register/', register_view, name="register"),
    path('products/', include('products.urls')),
    path('', home, name="home" )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
