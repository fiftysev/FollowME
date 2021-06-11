from django.urls import path
from .views import RegistrationUserView, UserListView

urlpatterns = [
    path('registration/', RegistrationUserView.as_view(), name='registration'),
    path('userlist/', UserListView.as_view(), name='UserList')
]
