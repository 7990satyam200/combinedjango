from django.urls import path
from .import views

urlpatterns = [
    path('network/', views.socialListView.as_view(), name='social'),
    path('profile/', views.Profile.as_view(), name='Profile'),

    path('<int:pk>', views.twitDetailView.as_view(), name='twit_detail'),
    path('new_tweet/', views.new_tweet.as_view(), name='new_tweets'),

    path('<int:pk>/edit', views.twitEditView.as_view(), name='twit_edit'),
    path('<int:pk>/delete', views.twitDeleteView.as_view(), name='twit_delete'),

]
