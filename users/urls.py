from django.urls import path, include
from .views import UserRegistrationView, UserAPIListView

urlpatterns = [
    path('list/', UserAPIListView.as_view(), name='user-list'),
    path('register/', UserRegistrationView.as_view(), name='user-create'),
    path('', include('rest_framework.urls')),

]
