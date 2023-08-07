from django.urls import path
from .views import categoryViewSet, brandViewSet, productViewSet


urlpatterns = [
    path('category/', categoryViewSet.as_view({'get': 'list'})),
    path('brand/', brandViewSet.as_view({'get': 'list'})),
    path('product/', productViewSet.as_view({'get': 'list'})),
]