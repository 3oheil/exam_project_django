from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelDashboard.as_view(), name='panel_dashboard'),
    path('edit-profile', views.UserEditProfileView.as_view(), name='edit_profile_page'),
    path('change-password', views.ChangePasswordView.as_view(), name='change_password_page'),
]
