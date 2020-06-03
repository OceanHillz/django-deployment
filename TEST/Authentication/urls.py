from django.urls import path
from .views import index, user_login, user_logout, register_user

app_name='authenticate'

urlpatterns = [
    path('', index, name="home"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('register/', register_user, name="register")
]
