"""
Custom Exception handler functions
"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """
    Default exception handler so that api consumer will get uniform response in any condition

    If any exception is raised and response object exists then return otherwise
    create response object , set status code to 500 and then return.

    .. note::
       This could have been implemented in better way like uniform response irrespective of
       what exception is thrown and logger could have been put here but this is just a
       demo project so no production grade methods are implemented

    """
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.

    # to logging here
    if response is not None:
        response.data['status_code'] = response.status_code
    else:
        response = Response({"errors": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
