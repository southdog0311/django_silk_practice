from django.urls import path, include
from .views import home_view, redirect_url_view
from .api import api
 
appname = "shorter"
 
urlpatterns = [
    # Home view
    path("", home_view, name="home"),
    path('<str:shorted_part>', redirect_url_view, name='redirect'),
    path('api/', api.urls), 
    path('silk/', include('silk.urls', namespace='silk')),
]

