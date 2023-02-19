from django.urls import path, re_path
from .views import *
from django.contrib.auth.views import (
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordResetDoneView,
    LogoutView,
)

urlpatterns = [
    path("register", register, name="register"),
    re_path(
        r"^activate/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$",
        account_activation,
        name="activate",
    ),
    path("login", login_view, name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("password-reset", reset_password, name="password_reset"),
    path(
        "password-reset/<uidb64>/<token>",
        PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/done",
        PasswordResetDoneView.as_view(template_name="password_reset_done.hmtl"),
        name="password_reset_done",
    ),
    path(
        "password-reset-complete",
        PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
        name="password_reset_complete",
    ),
]
