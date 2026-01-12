from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache

from messenger.models import Message
from messenger.tasks import send_notification


@receiver(post_save, sender=Message)
def new_message_notification(sender, instance, created, **kwargs):
    if created:
        send_notification.delay(instance.id)


@receiver(post_save, sender=Message)
def invalidate_message_cache(*args,**kwargs):
    cache.delete_pattern("*messages*")
