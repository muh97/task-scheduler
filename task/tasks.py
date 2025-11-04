from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Task
import time


@shared_task
def process_task(task_id):
    try:
        task = Task.objects.get(id=task_id)
        time.sleep(5)
        task.status = 'completed'
        task.completed_at = timezone.now()
        task.save()
        return f"Task {task_id} completed successfully"
    except Task.DoesNotExist:
        return f"Task {task_id} not found"


@shared_task
def cleanup_old_completed_tasks():
    one_hour_ago = timezone.now() - timedelta(hours=1)
    deleted_count, _ = Task.objects.filter(
        status='completed',
        completed_at__lt=one_hour_ago
    ).delete()
    return f"Deleted {deleted_count} old completed tasks"

