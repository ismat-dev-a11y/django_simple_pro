from django.urls import path
from .views import *

urlpatterns = [
    path("simple", SimplePage.as_view(), name="simple"),
    path("register/", RegisterView.as_view(), name="register"),
    path("", Login_View.as_view(), name="login"),
    path('logout/', logout_view, name='logout')

]
