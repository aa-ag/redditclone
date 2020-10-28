from django.contrib import admin
from django.urls import path
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', account.views.signup, name='signup'),
]
