from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.get_homepage, name='homepage'),
    path('logout', views.logout_user, name='logout')
]

