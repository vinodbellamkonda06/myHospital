from django.conf.urls import url
from . import views


urlpatterns = [
    url('just', views.justtest),
]