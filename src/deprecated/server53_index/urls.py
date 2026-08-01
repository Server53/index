"""
URL configuration for server53_index project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from src.deprecated.filestore.urls import urlpatterns as filestore_urls
from src.deprecated.minecraft.views import ModPacksListView, ServersListView

urlpatterns = [
    path('servers/', ServersListView.as_view()),
    path('modpacks/<int:server_id>/', ModPacksListView.as_view()),
    path('admin/', admin.site.urls),
    path('files/', include(filestore_urls))
]
