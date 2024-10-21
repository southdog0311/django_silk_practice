from django.urls import path
from .views import home_view, redirect_url_view
 
appname = "shorter"
 
urlpatterns = [
    # Home view
    path("", home_view, name="home"),
    path('<str:shorted_part>', redirect_url_view, name='redirect'),
]