from django.urls import path
from . import views


urlpatterns = [
    path("", views.product_detail_view, name = "product"),
    path("create/", views.create_view, name="create")
]