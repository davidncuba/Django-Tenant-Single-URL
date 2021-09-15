from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from client.models import Client
from client.serializers import ClientSerializer
from django.core.exceptions import ObjectDoesNotExist


class ClientViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ClientSerializer

    def create(self, request):

        client = request.data or {}
        tenant_name = client.get("tenant_name")

        if tenant_name is None:

            raise ValidationError("A tenant name is mandatory.")
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            tenant = Client.objects.get(tenant_name=tenant_name)

        except ObjectDoesNotExist:
            raise ValidationError("A tenant name not exist")

        serializer = self.serializer_class(tenant, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
