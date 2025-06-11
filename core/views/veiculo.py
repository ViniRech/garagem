from rest_framework.viewsets import ModelViewSet

from core.models import Veiculo
from core.serializers import VeiculoListRetrieveSerializer, VeiculoSerializers


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializers

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return VeiculoListRetrieveSerializer
        return VeiculoSerializers
