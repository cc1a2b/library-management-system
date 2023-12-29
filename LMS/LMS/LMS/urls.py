from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.admin import UserAdmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_user/', include('user_managment.urls')),
    path('api_book/', include('book_managment.urls')),
]
