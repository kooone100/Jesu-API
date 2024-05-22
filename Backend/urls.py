from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Store.urls')),
    path('auth-api/', include('rest_framework.urls')),
]
