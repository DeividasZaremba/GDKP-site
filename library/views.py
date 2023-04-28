from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import WowChar, WowPlayer, EventRegistration
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from datetime import date
from .forms import MyUserCreationForm, EventRegistrationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views import View
from django.http import HttpResponseRedirect

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


def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = MyUserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})


@login_required
def user_profile(request):
    player, created = WowPlayer.objects.get_or_create(user=request.user, defaults={'nickname': request.user.username})
    context = {'player': player}
    return render(request, 'user_profile.html', context)


class UserProfileUpdate(LoginRequiredMixin, UpdateView):
    model = WowPlayer
    fields = ['discord_tag', 'description', 'gold']
    template_name = 'user_profile_update.html'

    def get_object(self, queryset=None):
        return self.request.user.wowplayer

    def get_success_url(self):
        return reverse_lazy('user_profile')


class UserCreateCharacter(LoginRequiredMixin, CreateView):
    model = WowChar
    fields = ['char_title', 'char_class', 'char_spec']
    template_name = 'user_create_character.html'

    def form_valid(self, form):
        form.instance.wow_player = self.request.user.wowplayer
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user_profile')


class UserDeleteCharacter(LoginRequiredMixin, DeleteView):
    model = WowChar
    template_name = 'user_delete_character.html'
    success_url = reverse_lazy('user_profile')
    
    def get_queryset(self):
        return super().get_queryset().filter(wow_player=self.request.user.wowplayer)
    

class RegisterEventView(UserPassesTestMixin, View):
    raise_exception = True

    def test_func(self):
        return self.request.user.groups.filter(name='Leader').exists()

    def get(self, request, *args, **kwargs):
        form = EventRegistrationForm()
        return render(request, 'event_registration_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event-list')
        return render(request, 'event_registration_form.html', {'form': form})
    
def handler403(request, exception=None):
    return render(request, '403.html', status=403)


@login_required
def sign_event(request, event_id):
    event = get_object_or_404(EventRegistration, id=event_id)
    wow_player = request.user.wowplayer
    event.registered_players.add(wow_player)
    event.save()
    return HttpResponseRedirect(reverse('event_details', args=[str(event_id)]))

@login_required
def unsign_event(request, event_id):
    event = get_object_or_404(EventRegistration, pk=event_id)
    player = request.user.wowplayer
    event.registered_players.remove(player)
    return HttpResponseRedirect(reverse('event_details', args=[str(event_id)]))