from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import WowChar, WowClass, WowPlayer, WowSpec, CharInstance, EventRegistration
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Q
from django.utils import timezone
from datetime import date


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
    
    def get_events_by_days(self):
        events = EventRegistration.objects.filter(event_date__gte=date.today())
        sorted_dict = {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': [],
            'Saturday': [],
            'Sunday': []
        }

        for event in events:
            event_weekday = event.event_date.weekday()
            match event_weekday:
                case 0:
                    sorted_dict['Monday'].append(event)
                case 1:
                    sorted_dict['Tuesday'].append(event)
                case 2:
                    sorted_dict['Wednesday'].append(event)
                case 3:
                    sorted_dict['Thursday'].append(event)
                case 4:
                    sorted_dict['Friday'].append(event)
                case 5:
                    sorted_dict['Saturday'].append(event)
                case 6:
                    sorted_dict['Sunday'].append(event)
        return sorted_dict

    def get_queryset(self):
        return self.get_events_by_days()



class EventRegistrationDetailView(DetailView):
    model = EventRegistration
    template_name = 'event_details.html'


def search(request):
    query = request.GET.get('query')
    search_results = WowPlayer.objects.filter(Q(nickname__icontains=query))
    return render(request, 'search.html', {'entries': search_results, 'query': query})



def event_details(request, event_id):
    event = get_object_or_404(EventRegistration, id=event_id)
    context = {'event': event}
    return render(request, 'event_details.html', context)