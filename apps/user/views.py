from rest_framework import generics

from apps.user.models import User
from apps.user.serializers import ConsultantsSerializers


class ConsultantsListView(generics.ListAPIView):
    serializer_class = ConsultantsSerializers
    queryset = User.objects.all()
