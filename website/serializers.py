from rest_framework import serializers
from farmsetu.type_class import *


class ClimateApiSerializer(serializers.Serializer):
    """
    Take input from user for meetoffice api

    .. seealso::

       :class:`farmsetu.type_class.OrderType`
       :class:`farmsetu.type_class.RegionType`
       :class:`farmsetu.type_class.ParameterType`
    """
    #: values from :class:`farmsetu.type_class.OrderType`
    order = serializers.ChoiceField(choices=OrderType.choices)
    #: values from :class:`farmsetu.type_class.RegionType`
    region = serializers.ChoiceField(choices=RegionType.choices)
    #: values from :class:`farmsetu.type_class.ParameterType`
    parameter = serializers.ChoiceField(choices=ParameterType.choices)
