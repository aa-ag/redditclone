from django.urls import path, include
from django.contrib import admin
from posts import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('posts/', include('posts.urls')),
    path('', views.home, name="home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
