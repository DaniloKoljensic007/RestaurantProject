from django.urls import path
from menu import views

urlpatterns = [
    path('menu/', views.MenuItemViewSet.as_view({"get": 'list'}))

]