import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # request.body
    # print(dir(request))
    print(request.GET) # url query params 
    print(request.POST)

    body = request.body # byte string of JSON Data
    data = {}
        
    try:
        data = json.loads(body) # string of JSON -> Python Dict
    except:
        pass

    print(data)
    
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content'] = request.content_type
    
    return JsonResponse(data)