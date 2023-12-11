from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
 
from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    Django Rest API View
    """

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)

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