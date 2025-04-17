from rest_framework.serializers import ModelSerializer

from core.models import Modelo


class ModeloSerializers(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"
