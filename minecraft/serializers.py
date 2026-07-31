from rest_framework import serializers

from .models import MCModPack, MCServer


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCServer
        fields = '__all__'


class ModPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCModPack
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('server', None)
        return representation
