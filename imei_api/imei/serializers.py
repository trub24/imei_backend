from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class CheckImeiSerializer(serializers.Serializer):
    imei = serializers.CharField(max_length=15)

    def validate_imei(self, value):
        if len(value) > 8 and len(value) < 15 and value.isdigit():
            return value
        raise serializers.ValidationError("IMEI должен быть от 8 до 15 символов и состоять только из цифр!")


class CheckWhiteListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'tg_id',
        )
