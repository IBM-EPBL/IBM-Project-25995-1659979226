from django.urls import path
from . import views
from knox import views as knox_views

urlpatterns = [
    path('login',views.login_user),
    path('user',views.get_user_detail),
    path('register',views.register_user),
    path('getotp',views.get_otp),
    path('verifyotp',views.verify_otp),
    path('updatepassword',views.update_password),
    path('updatephno',views.update_phonenumber),
    path('logout',knox_views.LogoutView.as_view()),
    path('logoutall',knox_views.LogoutAllView.as_view()),
]
