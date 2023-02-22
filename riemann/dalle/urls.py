from django.urls import path, re_path
from .views import *
from django.conf import settings
from django.views.static import serve as mediaserve

urlpatterns = [
    path('', index, name='main'),
    path('dalle/', dalle, name='dalle'),
    path('help/', help, name='help'),
]

# urlpatterns += [
#     re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$', mediaserve, {'document_root': settings.MEDIA_ROOT}),
#     re_path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$', mediaserve, {'document_root': settings.STATIC_ROOT})
# ]