from django.urls import path
from .views import ВookCreateView

urlpatterns = [
    path("", ВookCreateView.as_view(), name="home"),
]
