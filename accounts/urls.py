from django.urls import path
from .views import signup_view, login_view, logout_view,dashboard_view,index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    
]
