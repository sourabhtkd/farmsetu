from rest_framework import serializers
from farmsetu.type_class import *


class ClimateApiSerializer(serializers.Serializer):
    order = serializers.ChoiceField(choices=OrderingType.choices)
    region = serializers.ChoiceField(choices=RegionType.choices)
    parameter = serializers.ChoiceField(choices=ParameterType.choices)

    def save(self, **kwargs):
        super().save()

    def create(self, validated_data):
        super(ClimateApiSerializer, self).create(**validated_data)

    def update(self, instance, validated_data):
        super(ClimateApiSerializer, self).update(*instance, **validated_data)
