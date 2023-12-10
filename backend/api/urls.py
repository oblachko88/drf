from django.urls import path

from . import views
# Or from .views import api_home

urlpatterns = [
    path('', views.api_home) # So here we can just use the api_home function that we could import from .views
    # This also would be the localhost:8000/api/
]


