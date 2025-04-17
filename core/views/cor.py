from rest_framework.viewsets import ModelViewSet

from core.models import Cor
from core.serializers import CorSerializers


class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializers
