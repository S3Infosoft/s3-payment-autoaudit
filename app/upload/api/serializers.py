from rest_framework import serializers

from ..models import Type1, Type8, Type9, Customer


class CustomerNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "name",

    def to_representation(self, instance):
        return instance.name, instance.id


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


class Type9Serializers(serializers.ModelSerializer):
    """Serializer for Type9 data"""

    class Meta:
        model = Type9
        fields = "__all__"
