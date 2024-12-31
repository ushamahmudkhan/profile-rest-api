from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of API View Features"""
        an_apiview = [
            'Uses HTTP Method as function(get, post, patch, put, delete)',
            'Is similiar to traditional Django View',
            'Gives You the best control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})
