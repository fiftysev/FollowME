from django.urls import path
from .views import RegistrationUserView

urlpatterns = [
    path('registration/', RegistrationUserView.as_view(), name='registration'),
]
