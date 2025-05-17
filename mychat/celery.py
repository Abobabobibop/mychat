import os
from celery import Celery
from kombu import Queue, Exchange

# Вказуємо налаштування Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mychat.settings')

app = Celery('mychat')

# Зчитуємо налаштування з settings.py, які починаються з префіксу CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Оголошуємо окремі черги
app.conf.task_queues = (
    # Черга для розсилки email
    Queue('email', Exchange('email'), routing_key='email'),
    # Черга для довготривалих тасків
    Queue('long_tasks', Exchange('long_tasks'), routing_key='long_tasks'),
)

# За бажанням – щоб всі незамаршрутизовані таски йшли в default
app.conf.task_default_queue = 'default'
app.conf.task_default_exchange = 'default'
app.conf.task_default_routing_key = 'default'

# (Опціонально) Можна задати правила маршрутизації на рівні імені таска
app.conf.task_routes = {
    'your_app.tasks.send_group_email': {'queue': 'email',      'routing_key': 'email'},
    'your_app.tasks.long_task':       {'queue': 'long_tasks', 'routing_key': 'long_tasks'},
}

# Шукаємо всі tasks.py у піддодатках
app.autodiscover_tasks()
