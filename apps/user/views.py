from rest_framework import generics

from apps.answersage.models import Question
from apps.user.models import User
from apps.user.serializers import ConsultantSerializer, ConsultationsListSerializer, ConsultationsCreateSerializer


class ConsultantsList(generics.ListAPIView):
    serializer_class = ConsultantSerializer
    queryset = User.objects.all()


class ConsultationsList(generics.ListAPIView):
    serializer_class = ConsultationsListSerializer
    queryset = User.objects.all()


class ConsultationsDetail(generics.RetrieveAPIView):
    serializer_class = ConsultationsListSerializer
    queryset = User.objects.all()


class ConsultantsCreate(generics.CreateAPIView):
    serializer_class = ConsultationsCreateSerializer
    queryset = Question.objects.all()
