from django.urls import path
from . import views 

urlpatterns = [
    #Home and Dashboard views 
    path('', views.home, name='home'),
    
    #Login, Register and Logout views 
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # MVT Tasks - Views of Donation
    path('donation/', views.donation, name='donation'),
    path('crisis/', views.crisis, name='crisis'),
    
    #Admin section views
    path('admin_panel/crisis/', views.admin_crisis, name = 'admin_crisis'),
    path('admin_panel/crisis/approve/<int:crisis_id>/', views.admin_approve_crisis, name = 'approve_crisis'),
    path('admin_panel/crisis/update/<int:crisis_id>/', views.admin_update_crisis, name = 'update_crisis'),
]