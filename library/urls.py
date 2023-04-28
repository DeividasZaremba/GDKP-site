from django.urls import path, include
from .views import event_details
from . import views
from .views import EventRegistrationListView, EventRegistrationDetailView, UserProfileUpdate, UserCreateCharacter


urlpatterns = [
    path('', views.index, name='index'),
    path('players/', views.players, name='players'),
    path('players/<int:player_id>', views.player, name='player'),
    path('events/', EventRegistrationListView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventRegistrationDetailView.as_view(), name='event_details'),
    path('events/', views.events, name='events'),
    path('search/', views.search, name='search'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('user_profile/update/', UserProfileUpdate.as_view(), name='user_profile_update'),
    path('user_profile/update/', UserProfileUpdate.as_view(), name='user_profile_update'),
    path('user_profile/create_character/', UserCreateCharacter.as_view(), name='user_create_character'),
    path('register_event/', views.RegisterEventView.as_view(), name='register_event'),
    path('sign_event/<int:event_id>/', views.sign_event, name='sign_event'),
    path('unsign_event/<int:event_id>/', views.unsign_event, name='unsign_event'),
]