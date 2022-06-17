from rest_framework.serializers import ModelSerializer
from .models import *

class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class CorporationSerializer(ModelSerializer):
    class Meta:
        model = Corporation
        fields = '__all__'

class ManagerSerializer(ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'