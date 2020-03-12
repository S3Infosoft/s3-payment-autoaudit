from rest_framework import serializers

from ..models import Type1


class Type1Serializers(serializers.ModelSerializer):
    class Meta:
        model = Type1
        fields = "__all__"
