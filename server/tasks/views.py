from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from auditlog.models import LogEntry

from tasks.models import Task, Task_Status, Categorie
from tasks.serializers import TaskSerializer, TaskStatusSerializer, CategorieSerializer, AuditLogSerializer



# View ou Create tasks
@api_view(['GET', 'POST'])
def tasks(request):

    # verify if method is a GET requisition
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # verify if method is a POST requisition
    elif request.method == 'POST':
        task_serialized = TaskSerializer(data = request.data)

        if task_serialized.is_valid():
            task_serialized.save() 
            return Response(task_serialized.data, status=status.HTTP_201_CREATED)
    
        return Response(task_serialized.errors, status=status.HTTP_400_BAD_REQUEST)




# View Details, Edit or Delete task
@api_view(['GET', 'PUT', 'DELETE'])
def tasks_detail(request, pk):

    try:
        task = Task.objects.get(pk = pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Return task detail
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()

        return Response(status=status.HTTP_200_OK)




# Return all changes made in the task
@api_view(['GET'])
def task_detail_log(request, pk):
    try:
        loggs = LogEntry.objects.filter(object_pk=pk).order_by('timestamp')
    except LogEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = AuditLogSerializer(loggs, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)




# View ou Create categories
@api_view(['GET', 'POST'])
def categories(request):

    # verify if method is a GET requisition
    if request.method == 'GET':
        categories = Categorie.objects.all()
        serializer = CategorieSerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # verify if method is a POST requisition
    elif request.method == 'POST':
        categorie_serialized = CategorieSerializer(data = request.data)

        if categorie_serialized.is_valid():
            categorie_serialized.save() 
            return Response(categorie_serialized.data, status=status.HTTP_201_CREATED)
    
        return Response(categorie_serialized.errors, status=status.HTTP_400_BAD_REQUEST)




# View Details, Edit or Delete categories
@api_view(['GET', 'PUT', 'DELETE'])
def categories_detail(request, pk):

    try:
        categories = Categorie.objects.get(pk = pk)
    except Categorie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Return task detail
    if request.method == 'GET':
        serializer = CategorieSerializer(categories)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = CategorieSerializer(categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        categories.delete()
        return Response(status=status.HTTP_200_OK)




# View ou Create tasks-status
@api_view(['GET', 'POST'])
def task_status(request):

    # verify if method is a GET requisition
    if request.method == 'GET':
        tasks_status = Task_Status.objects.all()
        serializer = TaskStatusSerializer(tasks_status, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # verify if method is a POST requisition
    elif request.method == 'POST':
        tasks_status_serialized = TaskStatusSerializer(data = request.data)

        if tasks_status_serialized.is_valid():
            tasks_status_serialized.save() 
            return Response(tasks_status_serialized.data, status=status.HTTP_201_CREATED)
    
        return Response(tasks_status_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    



# View Details, Edit or Delete task-status
@api_view(['GET', 'PUT', 'DELETE'])
def task_status_detail(request, pk):

    try:
        task_status = Task_Status.objects.get(pk = pk)
    except Task_Status.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Return task detail
    if request.method == 'GET':
        serializer = TaskStatusSerializer(task_status)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = TaskStatusSerializer(task_status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task_status.delete()
        return Response(status=status.HTTP_200_OK)