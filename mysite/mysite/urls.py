from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('main/', include('main.urls')),
    path('', include('common.urls')),
    path('common/', include('common.urls')),
    path('admin/', admin.site.urls),
]
