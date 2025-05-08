
from django.contrib import admin
from django.urls import path
from .views import getresults,register,success,dashboard_view,plotly_view,pandas_view,FileUploadView
urlpatterns = [
    path('getresults/', getresults, name='getresults'),
    path('register/', register, name='register'),
    path('success/', success, name='success'),  
    path('dashboard/',dashboard_view,name='dashboard'),
    path('plotly/',plotly_view,name='plotly'),
    path('pandas/',pandas_view,name='pandas'),
    path('fileupload/',FileUploadView.as_view(),name='fileupload'),
]

