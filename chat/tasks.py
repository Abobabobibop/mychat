from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.utils import timezone

@shared_task(queue='email')
def send_group_email(subject, message, group_name):
    users = Group.objects.get(name=group_name).user_set.all()
    for u in users:
        send_mail(
            subject,
            message,
            'from@example.com',
            [u.email],
            fail_silently=False
        )

@shared_task(queue='long_tasks')
def long_task(data):
    # Емітація тривалої обробки
    result = data[::-1]

    # Повідомлення через WebSocket після завершення
    layer = get_channel_layer()
    async_to_sync(layer.group_send)(
        'admin_notifications',           # назва групи каналу
        {
            'type': 'task_update',       # має збігатися з ім’ям методу consumer
            'data': {
                'operation': 'long_task',
                'input': data,
                'result': result,
                'timestamp': timezone.now().isoformat()
            }
        }
    )
    return result
