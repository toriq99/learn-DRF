import json
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def api_home(request, *args, **kwargs):
    # request -> HTTPResponse -> Django
    print(request.GET)                  # url query params
    print(request.POST)                 

    body = request.body
    data = {}

    try:
        data = json.loads(body)         # strinf JSON data -> Python Dict
    except:
        pass

    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse(data)