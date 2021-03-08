from django.urls import path
from .views import *


app_name = 'app'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('dashboard', DashboardView.as_view(), name="dashboard"),
    path('signin', SigninView.as_view(), name="signin"),
    path('signup', SignupView.as_view(), name="signup"),
    path('table', TableView.as_view(), name="table"),
    path('form', FormView.as_view(), name="form"),
    path('404', NotFoundView.as_view(), name="404"),
]