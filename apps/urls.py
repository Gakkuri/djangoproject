from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cell_update/<int:row>/<int:col>", views.cell_update, name="cell_update"),
    path("lock_update/<int:row>/<int:col>", views.lock_update, name="lock_update"),
]
