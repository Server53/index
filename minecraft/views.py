from django import views
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import MCModPack, MCServer
from .serializers import ModPackSerializer, ServerSerializer


class ServersListView(generics.ListAPIView):
    queryset = MCServer.objects.all()
    serializer_class = ServerSerializer


class ModPacksListView(generics.ListAPIView):
    serializer_class = ModPackSerializer

    def get_queryset(self):
        """ Return modpacks for required server_id. """
        server_id = self.kwargs['server_id']
        return MCModPack.objects.filter(server_id=server_id)
