from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.predict_yield, name='predict_yield'),  # Add this line
    # path('login/', views.login_view, name='login'),
    # path('signup/', views.signup_view, name='signup'),
    # path('logout/', views.logout_view, name='logout'),
    # path('changepassword/', views.change_password, name='changepassword'),
]
