from django.urls import path, include
from .views import (UserViewSet, MeasurementViewSet, CustomersViewSet)
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('customer', CustomersViewSet, basename='customer')
router.register('measure', MeasurementViewSet, basename='measure')
router.register('users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls))
    # path('customers/', views.CustomersList.as_view()),
    # path('customer/<int:pk>/', views.CustomersDetailList.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
