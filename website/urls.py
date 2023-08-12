from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name= 'home'),
    path('login', views.login_user, name ='login' ),
    path('logout', views.logout_user, name ='logout' ),
    path('register', views.register, name ='register' ),
    path('customer/<int:pk>', views.customer, name ='customer' ),
    path('delete/<int:pk>', views.delete, name ='delete' ),





]
