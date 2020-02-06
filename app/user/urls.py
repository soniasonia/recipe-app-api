from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token')
    # name is used to identify when we use reverse function
]
# When we create our client app that consumes the API
# we would take the token and store in the cookie or system storage
# to authenthicate future requests
