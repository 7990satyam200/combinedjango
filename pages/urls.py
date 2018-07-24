from django.urls import path, include
from .import views

urlpatterns=[
    path('', views.home.as_view(), name='home'),
    path('registerS/', views.signup, name='new_register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
