from django.urls import path
from mobile.views import hello
urlpatterns = [
    path('', hello,name='hello'),
]
