from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('signin/', views.signin, name = 'signin'),
    path('release/<int:release_id>/', views.release_detail, name='release_detail'),
    path('release/<int:release_id>/add-comment/', views.add_comment, name='add_comment'),
    path('about/', views.about, name = 'about'),
    
]