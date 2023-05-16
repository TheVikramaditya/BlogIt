from django.urls import path
from . views import SignUp,LogIn,LogOut

app_name = 'accounts'

urlpatterns = [
    path('',LogIn,name="login"),
    path('signup/',SignUp,name="signup"),
    path('logout/',LogOut,name="logout"),
]