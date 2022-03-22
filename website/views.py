import traceback

import requests
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.renderers import HTMLFormRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from website import serializers as website_serializers
from farmsetu import constants
from website.utils.climate_api_utils import ClimateApiUtil


class MetOfficeView(APIView):
    """
    Calls MeetOffice api , parses data and returns it

    .. seealso::

       :class:`website.serializers.ClimateApiSerializer`

    """
    serializer_class = website_serializers.ClimateApiSerializer

    def post(self, request, *args, **kwargs):
        """
        accepts post request, validates data , calls api and send formatted response

        For more details check https://github.com/sourabhtkd/farmsetu

        """
        serializer = website_serializers.ClimateApiSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.validated_data['order']
            region = serializer.validated_data['region']
            parameter = serializer.validated_data['parameter']
            climate_api_util = ClimateApiUtil(parameter=parameter,
                                              ordering_type=order,
                                              region=region)
            response = dict()
            response['order'] = order
            response['region'] = region
            response['parameter'] = parameter
            climate_data = climate_api_util.get_climate_data()
            if climate_data.is_valid():
                formatted_data = climate_data.get_formatted_data()
                response['data'] = formatted_data
                return Response(response)
            else:
                return Response({"errors": climate_data.message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
