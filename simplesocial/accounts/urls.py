from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'


urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(template_name="accounts/login.html"),
         name="login"),
    # Default django - logout takes you to home page so no template_name has to be set
    path('logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),
    path('signup/',
         views.SignUp.as_view(),
         name='signup'),

]
