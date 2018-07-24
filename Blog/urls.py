from django.urls import path
from .import views

urlpatterns=[
    path('blog/', views.BlogHome.as_view(), name='Blog'),
    path('blog/<int:pk>/', views.Detail.as_view(), name='detail'),
    path('blog/new/', views.new.as_view(), name='new'),
    path('blog/edit/<int:pk>/', views.editView.as_view(), name='edit_blog'),
    path('blog/delte/<int:pk>/', views.deleteView.as_view(), name='delete_blog'),
    # path('signup', views.signup, name='signup'),


]
