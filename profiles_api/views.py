from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiVIew(APIView):
    """TEst API VIEW"""

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview=[
            'USe HTTP methos as function (get,post,put,delete)',
            'Is similar to tradininal Django View',
            "HEllo Djnaog REST Api"
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})