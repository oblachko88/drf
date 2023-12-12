from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # We can assign a user that can perform a create view like that. Rough example
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None: 
            content = title
        serializer.save(content=content)
        # send a DJango signal


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    # Product.objects.all(pk=12)

@api_view(['GET', 'POST'])
def product_alt_view(request, *args, **kwargs):
    method = request.method

    if method == 'GET':
        pass
        # url args??
        # get request -> detail view
        # list view -> list view
    if method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # instance = serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)
            # create an item 
