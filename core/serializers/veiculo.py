from rest_framework.serializers import ModelSerializer

from core.models import Veiculo


class VeiculoSerializers(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
