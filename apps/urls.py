
from django.contrib import admin
from django.urls import path

from apps.views import OrderListAPIView

urlpatterns = [
    path('order-list' , OrderListAPIView.as_view()),

]
