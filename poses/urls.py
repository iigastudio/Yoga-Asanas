from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),

    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('', views.poses, name="poses"),


    path('pose/<str:pk>/', views.pose, name="pose"),

    path('add_pose/', views.addPose, name="add_pose"),

    path('update_pose/<str:pk>/', views.updatePose, name="update_pose"),

    path('delete_pose/<str:pk>/', views.deletePose, name="delete_pose"),
]