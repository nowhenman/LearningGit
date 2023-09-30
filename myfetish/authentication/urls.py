from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('signup', views.auth_sign_up, name='signup'),
    path('login', views.auth_login, name='login')
]

# template login
# func login
# form
# func login
