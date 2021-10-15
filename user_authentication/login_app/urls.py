from django.urls import path
from login_app import views


#TEMPLATE URLS/
app_name = 'login_app'

urlpatterns=[
path('register/',views.register,name='register'),
path('logout/',views.user_logout,name='logout'),
path('other_page/',views.other_page,name='otherpage'),
path('login/',views.user_login,name='user_login'),
]
