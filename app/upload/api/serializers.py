from rest_framework import serializers

from ..models import Type1, Type8


class Type1Serializers(serializers.ModelSerializer):
    """Serializer for Type1 data"""

    class Meta:
        model = Type1
        fields = "__all__"


class Type8Serializers(serializers.ModelSerializer):
    """Serializer for Type8 data"""

    class Meta:
        model = Type8
        fields = "__all__"
