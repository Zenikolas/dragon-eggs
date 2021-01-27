from .celery import celery_app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)
quantity_of_eggs = 0


@celery_app.task
def count():
    global quantity_of_eggs
    quantity_of_eggs += 1
    return f"<h1 style='color:blue'>Hello, It's a dragon and I've got {quantity_of_eggs} eggs! They are huge!</h1>"