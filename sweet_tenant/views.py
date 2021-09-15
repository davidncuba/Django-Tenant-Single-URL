from .models import Sweet
from .serializers import SweetSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class SweetViewSet(generics.ListCreateAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer
    # permission_classes = [IsAdminUser]
