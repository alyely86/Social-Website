from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    # previous login url
	# path('login/',user_login,name='login'),

    #login / logout urls
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),

    path('', dashboard, name='dashboard'),
]