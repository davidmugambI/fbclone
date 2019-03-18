from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView,
    PasswordChangeDoneView, PasswordResetConfirmView, PasswordResetCompleteView)

app_name = 'accounts' # Namespacing
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name="logout"),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='profile'),
    re_path('profile/(?P<pk>\d+)/', views.view_profile, name='profile_with_pk'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/',views.change_password, name='change_password'),
    path('reset-password/', PasswordResetView.as_view(template_name ='account/reset_password.html',
                                                       success_url ='password_reset_done',
                                                       email_template_name = 'accounts/reset_password_email.html'),
                                                        name='password_reset'),
    path('reset-password/done/',PasswordChangeDoneView.as_view(template_engine='accounts/reset_password_done.html'),
         name='password_reset_done'),
    re_path('reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/',
            PasswordResetConfirmView.as_view(template_engine='accounts:reset_password_confirm.html',
                                             success_url='accounts:password_reset_complete'),
            name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(template_engine='accounts/reset_\
        password_complete.html'),name='password_reset_complete' ),
]