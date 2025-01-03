from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of API View Features"""
        an_apiview = [
            'Uses HTTP Method as function(get, post, patch, put, delete)',
            'Is similiar to traditional Django View',
            'Gives You the best control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        """Handle Updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update on object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello message"""

        a_viewset = [
            'Uses actions(list, create, retrieve, update, partial_update)',
            'Automatically Maps to URLs using router'
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset' : a_viewset})
    def create(self, request):
        """Create a new Hello message"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello{name}!'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by it ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle Updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle Updating part o an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle Removing an object"""
        return Response({'http_method': 'DELETE'})
