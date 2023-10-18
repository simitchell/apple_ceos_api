from rest_framework import viewsets
from .models import AppleCeo
from .serializers import AppleCeoSerializer

# Create your views here.
class CeoViewSet(viewsets.ModelViewSet):
    queryset = AppleCeo.objects.all().order_by('-year')
    serializer_class = AppleCeoSerializer