from django.urls import path
from . import views
urlpatterns =  [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('top-artists/', views.top_artists, name='top-artists'),
    path('top-tracks/', views.top_tracks, name='top-tracks'),
    path('track/<int:track_id>/', views.track_info, name='track-info'),
]