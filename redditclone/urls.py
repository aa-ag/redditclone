from django.urls import path, include
from django.contrib import admin
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('posts/', include('posts.urls')),
    path('', views.home, name="home"),
]
