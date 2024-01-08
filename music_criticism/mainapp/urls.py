from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('release/<int:pk>/', views.ReleaseDetailView.as_view(), name='release-detail'),
]