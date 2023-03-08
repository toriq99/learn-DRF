from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializers

# Create your views here.

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

product_create_view = ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

product_detail_view = ProductDetailAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
    """
    Optional for use
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

product_list_view = ProductListAPIView.as_view()


# using API View
# @api_view(['GET', 'POST'])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method

#     if method == 'GET':
#         if pk is not None:
#             # detail view
#             obj = get_object_or_404(Product, pk=pk)
#             data = ProductSerializers(obj, many=False).data
#             return Response(data)
#         # list view
#         queryset = Product.objects.all()
#         data = ProductSerializers(queryset, many=True).data
#         return Response(data)

#     if method =='POST':
#         # create an item
#         serializer = ProductSerializers(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             print(serializer.data)
    