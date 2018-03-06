from django.urls import  path
from page import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:cat_id>/", views.index, name = "index"),
    path("good/<int:good_id>/", views.good, name = "good"),
]
