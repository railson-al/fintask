from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status 
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from app_users.models import Sector, Sector_Employee
from app_users.serializers import UserSerializer, UserLoginSerializer, SectorSerializer, SectorEmployeeSerializer


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def users_view(request, *args, **kwargs):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

    elif request.method == 'POST':
        user = request.data
        serializer = UserSerializer(data=user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# Route to get token authentication (login)
@api_view(['POST'])
def user_authenticate(request):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data['user']

    token, created = Token.objects.get_or_create(user=user)
                                                 
    return Response({'token': token.key}, status=status.HTTP_200_OK)



 # Create and view sectors
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def sectors(request):

    if request.method == 'GET':
        sectors = Sector.objects.all().order_by('sector_description')
        serializer = SectorSerializer(sectors, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method =='POST':
        serializer = SectorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
