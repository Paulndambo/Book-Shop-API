from django.urls import path
from .import views

urlpatterns = [
    path("burgains/", views.BookBurgainAPIView.as_view(), name="burgains"),
    path("burgains/<int:pk>/", views.BookBurgainUpdateDestroyAPIView.as_view(), name="burgain-details"),
]