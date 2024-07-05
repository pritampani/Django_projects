from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index, name="index"),  # Use 'index' if this is your home view
    path('del/<int:item_id>/', views.remove, name="remove"),  # Ensure you use int if item_id is an integer
    path('admin/', admin.site.urls),
]
