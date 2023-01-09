import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from Extrahop_challange.utils import UserUtility
from django.core.exceptions import ObjectDoesNotExist
from Extrahop_challange.constants import FILE_PATH

class UserAPIView(APIView):
    """
    This class handles user crud operation
    """
    def get(self, request, **kwargs):
        """
        This function gets detailed data for user against a username
        """
        user_id = kwargs.get("user_id", None) 
        try:
            with open(FILE_PATH, "r") as file:
                for line in file.readlines():
                    if user_id and user_id == line.split(':')[0]:
                        result = UserUtility.get_formatted_user_data(line)
                        return Response(data={"result": result}, status=status.HTTP_200_OK)
                
                return Response(data={"message": "No user exist with gicen username"}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(data={"message": "No such file exist with given name"}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, **kwargs):
        """
        This function deletes the data against a username
        """
        user_id = kwargs.get("user_id", None)
        deleted = False

        try:
            with open(FILE_PATH, "r") as file:               
                lines = file.readlines()
                with open(FILE_PATH, "w") as f:
                    for line in lines:
                        if user_id and not user_id == line.strip("\n").split(':')[0]:
                            f.write(line)
                        else:
                            deleted = True
                    if deleted:
                        return Response(data={"message": "User has been removed"}, status=status.HTTP_200_OK)
                return Response(data={"message": "No user exist with given username"}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(data={"message": "No such file exist with given name"}, status=status.HTTP_400_BAD_REQUEST)

        