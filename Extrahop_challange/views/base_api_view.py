from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from Extrahop_challange.constants import FILE_PATH


class BaseAPIView(APIView):
    """
    This class handles the request on base url
    """
    def get(self, request):
        """
        This function handles the get request on base url
        """
        list_of_all_users = []
        try:
            with open(FILE_PATH, 'r') as file:
                list_of_all_users = [user.split(':')[0] for user in file.readlines()]
                return Response(data={"result": list_of_all_users}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(data={"message": "No such file exist with given name"}, status=status.HTTP_400_BAD_REQUEST)
        
    