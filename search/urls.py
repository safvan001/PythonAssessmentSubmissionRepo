

from django.contrib import admin
from django.urls import path
from search.views import *

urlpatterns = [
    path('',home,name='home'),
    path('search/',search_repositories,name='search')

]
