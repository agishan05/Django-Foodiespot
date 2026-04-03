from django.urls import path
from . import views

urlpatterns = [

    path('', views.intro, name='intro'),

    path('home/', views.home, name='home'),

    path('order/<int:id>/', views.order_food, name='order'),

    path('success/', views.success, name='success'),

]