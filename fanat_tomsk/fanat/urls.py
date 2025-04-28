from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.show_about, name='about'),
    path('coach/', views.show_coach, name='coach'),
    path('schedule/', views.schedule, name='schedule'),
    path('price/', views.price, name='price'),
    path('shop/', views.shop, name='shop'),
	path('login/', views.login, name='login')	
]
