"""
URL configuration for darshan project.

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
from django.urls import path
from home.views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/',dashboard,name="dashboard"),
    path('headerweb/' ,headerweb,name="headerweb"),
    path( 'shop1/' ,shop1,name="shop1"),
    path('shop2/' ,shop2,name="shop2"),
    path('delete/<int:id>/',delete_product, name='delete'),
    path('update/<int:id>/',update, name='update'),
    path('headerpro/' ,headerpro,name="headerpro"),
    path('project1/' ,project1,name="project1"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)