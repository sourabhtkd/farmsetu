import traceback

import requests
from django.shortcuts import render

# Create your views here.
from rest_framework.renderers import HTMLFormRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from website import serializers as website_serializers
from farmsetu import constants
from website.utils.climate_api_utils import ClimateApiUtil


class MetOfficeView(APIView):
    serializer_class = website_serializers.ClimateApiSerializer

    def get(self, request, *args, **kwargs):
        # url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Sunshine/date/East_Anglia.txt"
        # result = requests.get(url, headers={'Accept': "application/json"})
        # text_data = result.text
        # result_list = list()
        # row_list = text_data.splitlines()[5:]
        # # print(row_list)
        # field_list = row_list.pop(0)
        # # print(field_list)
        # column_list = [f.strip() for f in field_list.split(' ') if f.strip() != ""]
        #
        # i = 0
        # for row in row_list:
        #     row_values = [r.strip() for r in row.split(' ') if r.strip() != ""]
        #     result = dict(zip(column_list, row_values))
        #     if len(result) >= 12 and i == 0:
        #         data_list = row_values[1:13]
        #         data_list = [float(d) for d in data_list]
        #         print(sum(data_list))
        #
        #     i += 1
        #     result_list.append(result)

        return Response({'data': 'data'})

    def post(self, request, *args, **kwargs):
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
                return Response({"errors": climate_data.message})
        else:
            return Response({'errors': serializer.errors})
