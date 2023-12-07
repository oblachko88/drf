import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # request.body
    # print(dir(request))

    body = request.body # byte string of JSON Data
    data = {}

    try:
        data = json.loads(body) # string of JSON -> Python Dict
    except:
        pass

    print(data)
    return JsonResponse(data)