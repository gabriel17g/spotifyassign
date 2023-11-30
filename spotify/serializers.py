from rest_framework import serializers
from .models import Songs


class songserials(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = "__all__"