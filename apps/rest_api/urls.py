"""
This is the admin URL module.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django.urls import path
from . import views

app_name = 'rest_api'
urlpatterns = [

    # House URLS.
    path('house/',
         views.HouseList.as_view(),
         name='house_list'),
    path('house/create/',
         views.HouseCreate.as_view(),
         name='house_create'),
    path('house/update/<int:pk>',
         views.HouseUpdate.as_view(),
         name='house_update'),
    path('house/delete/<int:pk>',
         views.HouseDelete.as_view(),
         name='house_delete'),

    # Flat URLS.
    path('flat/',
         views.FlatList.as_view(),
         name='flat_list'),
    path('flat/create/',
         views.FlatCreate.as_view(),
         name='flat_create'),
    path('flat/update/<int:pk>',
         views.FlatUpdate.as_view(),
         name='flat_update'),
    path('flat/delete/<int:pk>',
         views.FlatDelete.as_view(),
         name='flat_delete'),

]
