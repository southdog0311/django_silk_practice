from django.urls import path, include
from . import views
from .api import api

app_name = "shorter"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('api/shorten/', views.api_shorten_url, name='api_shorten_url'),
    path('silk/', include('silk.urls',namespace='silk')),
    path('short-urls/', views.short_url_list_view, name='short_url_list'),
    path('<str:shorted_part>/', views.redirect_url_view, name='redirect_url'),
    
]

