from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .tasks import process_task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        task = self.get_object()
        if task.status == 'completed':
            return Response(
                {'error': 'Task is already completed'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        process_task.delay(task.id)
        
        return Response(
            {'message': 'Task processing started'}, 
            status=status.HTTP_202_ACCEPTED
        )
