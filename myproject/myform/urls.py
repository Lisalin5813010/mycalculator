from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    path(r'',  views.IndexPage.as_view(),name = 'index'),
]