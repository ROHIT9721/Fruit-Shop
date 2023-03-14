from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
   path('admin/', admin.site.urls),
    path('',views.home , name = 'home'),
    path('signin',views.createuser,name='sign'),
    path('login',views.user_log, name ='login'),
    path('superuser',views.admin , name = 'admin'),
    path('contact',views.contact , name = 'contact'),
    path('fruit',views.fruit , name = 'fruit'),
    path('service',views.service  , name = 'service'),
    path('orders',views.orders  , name = 'orders'),

    
]