from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

@receiver(post_save, sender=User)
def add_user_to_raider_group(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Raider')
        instance.groups.add(group)