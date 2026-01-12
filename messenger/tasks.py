from celery import shared_task


@shared_task
def send_notification(message_id: int):
    print("New message created")
