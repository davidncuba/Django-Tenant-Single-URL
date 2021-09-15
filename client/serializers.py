from rest_framework import serializers


class ClientSerializer(serializers.Serializer):
    tenant_uuid = serializers.UUIDField()
    tenant_name = serializers.CharField()
