from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import WowChar, WowClass, WowPlayer, WowSpec, CharInstance, EventRegistration
from django.shortcuts import render, get_object_or_404
from django.views import generic

def index(request):
    num_chars = WowChar.objects.all().count()
    num_players = WowPlayer.objects.count()
    num_events = EventRegistration.objects.all().count()
    
    context = {
        'num_chars': num_chars,
        'num_players': num_players,
        'num_events': num_events,
    }

    return render(request, 'index.html', context=context)

def players(request):
    players = WowPlayer.objects.all()
    context = {
        'players': players
    }
    print(players)
    return render(request, 'players.html', context=context)


def player(request, player_id):
    single_player = get_object_or_404(WowPlayer, pk=player_id)
    return render(request, 'player.html', {'player': single_player})


def events(request):
    context = {
        'events': events
    }
    return render(request, 'event.html', context=context)

class EventRegistrationListView(ListView):
    model = EventRegistration
    template_name = 'event_list.html'


class EventRegistrationDetailView(DetailView):
    model = EventRegistration
    template_name = 'event_detail.html'
