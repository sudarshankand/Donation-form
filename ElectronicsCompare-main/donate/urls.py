from django.urls import path
from . import views

urlpatterns = [
    path('donation/', views.donation_form, name='donation_form'),
    # Add a URL pattern for a success page if needed
    # path('donation_success/', views.donation_success, name='donation_success'),
]
