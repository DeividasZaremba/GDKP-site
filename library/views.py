from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import WowChar, WowClass, WowPlayer, WowSpec, CharInstance, EventRegistration
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Q
import calendar

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


def search(request):
    query = request.GET.get('query')
    search_results = WowPlayer.objects.filter(Q(nickname__icontains=query))
    return render(request, 'search.html', {'entries': search_results, 'query': query})

def calendar_view(request, year, month):
    # Convert year and month strings to integers
    year = int(year)
    month = int(month)
    
    # Get the calendar for the specified month
    cal = calendar.monthcalendar(year, month)
    
    # Create a list of lists to store the calendar days and their CSS classes
    days = []
    for week in cal:
        week_days = []
        for day in week:
            # Determine if this day is in the current month or a previous/next month
            if day == 0:
                week_days.append((' ', 'other-month'))
            elif day < 10:
                week_days.append((str(day), 'current-month single-digit'))
            else:
                week_days.append((str(day), 'current-month'))
        days.append(week_days)
    
    # Get the previous and next months
    prev_month = month - 1
    prev_year = year
    if prev_month == 0:
        prev_month = 12
        prev_year = year - 1
    
    next_month = month + 1
    next_year = year
    if next_month == 13:
        next_month = 1
        next_year = year + 1
    
    # Render the calendar template with the calendar and paging information
    return render(request, 'event_list.html', {
        'year': year,
        'month': month,
        'days': days,
        'prev_month': prev_month,
        'prev_year': prev_year,
        'next_month': next_month,
        'next_year': next_year,
    })