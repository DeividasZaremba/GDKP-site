from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User

class WowSpec(models.Model):
    name = models.CharField('Spec', max_length=20, help_text='Character specialization.')
    spec_img = models.ImageField('Spec_image', upload_to='specs', null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Spec'
        verbose_name_plural = 'Specs'
        ordering = ['name']


class WowClass(models.Model):
    name = models.CharField('Class', max_length=20, help_text='Character class.')
    class_img = models.ImageField('Class_image', upload_to='class', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'
        ordering = ['name']

class WowChar(models.Model):
    char_title = models.CharField('Character name', max_length=30)
    wow_player = models.ForeignKey('WowPlayer', on_delete=models.CASCADE, related_name='chars')
    char_class = models.ForeignKey('WowClass', on_delete=models.SET_NULL, null=True)
    char_spec = models.ManyToManyField(WowSpec, help_text='Select spec for this char.')

    def __str__(self):
        spec_names = [spec.name for spec in self.char_spec.all()]
        return f'{self.char_title} - {self.char_class} ({" / ".join(spec_names)})'

    def get_absolute_url(self):
        return reverse('char-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Char'
        verbose_name_plural = 'Chars'
        ordering = ['char_title']


class WowPlayer(models.Model):
    nickname = models.CharField('Nickname', max_length=30)
    discord_tag = models.CharField('Discord tag', max_length=30, null=True, blank=True)
    description = models.TextField('About you', max_length=2000, default='', null=True, blank='True')
    gold = models.IntegerField('How thick is your wallet', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    @property
    def wow_chars(self):
        return self.wow_char.all()

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        ordering = ['nickname']

    def get_absolute_url(self):
        return reverse('player-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.nickname}'

    def display_chars(self):
        return ', '.join(char.char_title for char in self.chars.all()[:3])
    display_chars.short_description = 'Chars'

    def get_registered_chars(self):
        registered_chars = []
        for registration in self.events_registered.all():
            registered_chars += list(registration.registered_players.filter(id=self.id).values_list('chars__char_title', flat=True))
        return registered_chars


class EventRegistration(models.Model):
    event_name = models.CharField('Event Name', max_length=50)
    event_date = models.DateTimeField('Event Date and Time', help_text='Select the event date and time')
    event_info = models.TextField('Event Info', max_length=1000, default='')
    registered_players = models.ManyToManyField(WowPlayer, related_name='events_registered', blank=True)

    def __str__(self):
        return f'{self.event_name} - {self.event_date}'

    class Meta:
        verbose_name = 'Event Registration'
        verbose_name_plural = 'Event Registrations'
        ordering = ['event_date']

    def get_absolute_url(self):
        return reverse('event-details', args=[str(self.pk)])

class CharInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique character ID.')
    char = models.ForeignKey('WoWChar', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField('Will be available.', null=True, blank=True)

    RAID_STATUS = (
        ('a', 'Available'),
        ('d', 'Done this week'),
        ('r', 'Rostered for this week'),
    )

    status = models.CharField(
        max_length=1,
        choices=RAID_STATUS,
        blank=True,
        default='a',
        help_text='Current status'
    )

    class Meta:
        ordering = ['due_back']
    
    def __str__(self):
        return f'{self.id} ({self.char.char_title})'