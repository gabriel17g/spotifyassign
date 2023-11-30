from django.urls import path
from .views import User_view, Admin_view, login, register



urlpatterns = [
    path("", User_view, name="home"),
    path("<int:id>/", Admin_view, name="admins"),
    path("login/", login, name="login"),
    path("signup/", register, name="signup")

]
