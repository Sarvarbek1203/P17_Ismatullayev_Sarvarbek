

from django.urls import path
from apps.views import StaffListView, CustomLoginView, RegisterFormView

urlpatterns = [
    path('', StaffListView.as_view(), name='staff_page'),
    path('login', CustomLoginView.as_view(next_page='login_page'), name='login_page'),
    path('register', RegisterFormView.as_view(), name='register_page'),


]
