from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


from . import views
# Or from .views import api_home

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', views.api_home), # So here we can just use the api_home function that we could import from .views
    # This also would be the localhost:8000/api/
    # path('products/', include('products.urls')), # or we define this url straight up here.
]


