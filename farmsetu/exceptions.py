from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.

    # to logging here
    if response is not None:
        response.data['status_code'] = response.status_code
    else:
        response = Response({"errors": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
