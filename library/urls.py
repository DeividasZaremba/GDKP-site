from django.urls import path, include

from . import views
from .views import EventRegistrationListView, EventRegistrationDetailView


urlpatterns = [
    path('', views.index, name='index'),
    path('players/', views.players, name='players'),
    path('players/<int:player_id>', views.player, name='player'),
    path('events/', EventRegistrationListView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventRegistrationDetailView.as_view(), name='event-detail'),
    path('events/', views.events, name='events'),
    path('search/', views.search, name='search'),
    path('accounts/', include('django.contrib.auth.urls')),
]