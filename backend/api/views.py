import json
from django.http import JsonResponse

from products.models import Product


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    # This order_by("?") means we take only one random object from all of them. 
    data = {} 

    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)

# def api_home(request, *args, **kwargs):
#     # request -> HttpRequest -> Django
#     # request.body
#     # print(dir(request))

#     print(request.GET) # url query params 
#     print(request.POST)

#     body = request.body # byte string of JSON Data
#     data = {}
        
#     try:
#         data = json.loads(body) # string of JSON -> Python Dict
#     except:
#         pass

#     print(data)
    
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content'] = request.content_type

#     return JsonResponse(data)