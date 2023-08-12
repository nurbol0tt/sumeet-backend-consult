from rest_framework import serializers

from apps.user.models import Consultant, User


class ConsultantsSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "photo"
        )
