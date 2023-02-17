import json
from django.shortcuts import render
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializers

# Create your views here.

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API view
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}

    if instance:
        # data = model_to_dict(model_data, fields=['id', 'title']) 
        data = ProductSerializers(instance).data
    return Response(data)