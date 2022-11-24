from django.urls import path

from . import views


urlpatterns = [
    # Register & Login
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    # Dashboard
    path('', views.home, name="home"),
    # Calls
    path('calls/', views.allCalls, name="all_calls"),
    path('new_call/', views.newCall, name='new_call'),
    path('upgrade_call/<str:pk>/', views.upgradeCall, name='upgrade_call'),
    path('on_scene/<str:pk>/', views.onScene, name='on_scene'),
    path('cancel/<str:pk>/', views.cancelCall, name='cancel'),
    # Walkins
    path('walkins/', views.allWalkins, name="all_walkins"),
    path('new_walkin/', views.newWalkin, name='new_walkin'),
    path('walkins/<str:pk>/', views.walkins, name="walkins"),
    path('walkin_notes/<str:pk>/', views.walkinNotes, name='walkin_notes'),
    # Responders
    path('responders/', views.allResponders, name="all_responders"),
    path('new_responder/', views.newResponder, name='new_responder'),
    path('update_responder/<str:pk>/', views.updateResponder, name='update_responder'),  
]