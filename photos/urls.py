from django.urls import path
from .import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('add_photo/', views.add_photo, name='add_photo'),
    path('view_photo/<str:pk>/', views.view_photo, name='view_photo'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)