"""
URL configuration for hello_world project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('home',views.home,name='home page'),
    #path('home', auth_views.LoginView.as_view(template_name='index.html'), name='home page'),
    path('result',views.result,name='Result search'),
    path('manage_wishlist',views.manage_wishlist,name='manage_wishlist'),
    path('edit',views.edit,name='edit'),
    path('logout',views.logout,name='logout'),
    path('update/<str:id>',views.update,name='update'),
    # path('alert',views.alert,name='alert'),
    path('alert_price',views.alert_price,name='alert_price'),
    path('profile',views.profile,name='Profile Page'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('expression',views.expression,name='expression value')
]
