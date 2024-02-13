from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['id', 'is_active', 'is_admin', 'last_login', 'date_joined']

        extra_kwargs = {
            "password":{"write_only": True},
        }

    def validate_phone_number(self, value):
        ...
        return value







