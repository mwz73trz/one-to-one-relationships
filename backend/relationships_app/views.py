from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class CorporationViewSet(ModelViewSet):
    queryset = Corporation.objects.all()
    serializer_class = CorporationSerializer

class ManagerViewSet(ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


