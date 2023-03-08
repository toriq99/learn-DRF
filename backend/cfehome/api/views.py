import json
from django.shortcuts import render
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from products.models import Product
from products.serializers import ProductSerializers

# Create your views here.

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API view
    """
    serialize = ProductSerializers(data=request.data)

    if serialize.is_valid(raise_exception=True):    # gunakan raise exception TRUE jika ingin melihat error (jika ada)
        # instance = serialize.save()
        print(serialize.data)
        return Response(serialize.data)