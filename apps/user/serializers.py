from rest_framework import serializers

from apps.answersage.models import Answer, Question
from apps.user.models import Consultant, User


class ConsultantSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Consultant
        fields = ('id', 'first_name', 'last_name', 'photo')

    def get_id(self, instance):
        return str(instance.id)

    def get_first_name(self, instance):
        return instance.first_name

    def get_last_name(self, instance):
        return instance.last_name

    def get_photo(self, instance):
        return 'http://127.0.0.1:8000/'+instance.photo.url


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'answer', 'created')


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer()
    topic = serializers.CharField(source='get_topic_display')

    class Meta:
        model = Question
        fields = ('id', 'topic', 'text', 'result', 'created', 'answer')


class ConsultationsListSerializer(serializers.ModelSerializer):
    consultant = serializers.SerializerMethodField()
    consultations = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('consultant', 'consultations')

    def get_consultant(self, obj):
        consultant_data = {
            'id': obj.id,
            'first_name': obj.first_name,
            'last_name': obj.last_name,
            'photo': 'http://127.0.0.1:8000/'+obj.photo.url if obj.photo else None
        }
        return consultant_data

    def get_consultations(self, obj):
        consultations = obj.consultations.all().order_by('-created')
        return QuestionSerializer(consultations, many=True).data


class ConsultationsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('consultant', 'topic', 'text', 'result')
