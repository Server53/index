from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import MCModPack, MCServer
from .serializers import ModPackSerializer, ServerSerializer


from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import MCModPack, MCServer
from .serializers import ModPackSerializer, ServerSerializer


class ServersListView(generics.ListAPIView):
    queryset = MCServer.objects.all()
    serializer_class = ServerSerializer
    permission_classes = [AllowAny]  # Anyone can list


class ModPacksListView(generics.ListAPIView):
    serializer_class = ModPackSerializer
    permission_classes = [AllowAny]  # Anyone can list

    def get_queryset(self):
        """ Return modpacks for required server_id. """
        server_id = self.kwargs['server_id']
        return MCModPack.objects.filter(server_id=server_id)


class ServersViewSet(viewsets.ModelViewSet):
    queryset = MCServer.objects.all()
    serializer_class = ServerSerializer

    def get_permissions(self):
        """ 
        Instantiates and returns the list of permissions that this view requires.
        - AllowAny for 'list' action
        - IsAdminUser for all other actions
        """
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class ModPacksViewSet(viewsets.ModelViewSet):
    serializer_class = ModPackSerializer

    def get_queryset(self):
        """ Return modpacks for required server_id. """
        server_id = self.kwargs['server_id']
        return MCModPack.objects.filter(server_id=server_id)

    def get_permissions(self):
        """ 
        Instantiates and returns the list of permissions that this view requires.
        - AllowAny for 'list' action
        - IsAdminUser for all other actions
        """
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
