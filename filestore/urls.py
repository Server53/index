from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_admin_panel),
    path('upload/', views.upload_file),
    path('<str:file_id>', views.get_file),
]
