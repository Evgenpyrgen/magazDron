from django.urls import  path
#from page import views
from page.twviews import GoodListView, GoodDetailView


urlpatterns = [
    path("", GoodListView.as_view(), name = "index"),
    path("<int:cat_id>/", GoodListView.as_view(), name = "index"),
    path("good/<int:good_id>/", GoodDetailView.as_view(), name = "good"),
]
"""
urlpatterns = [
    re_path(r'^/$', GoodListView.as_view(), name = "index"),
    re_path(r'^(?:(?P<int:cat_id>\d+)/)?$', GoodListView.as_view(), name = "index"),
    re_path(r'^good/(?P<int:good_id>\d+)/$', GoodDetailView.as_view(), name = "good"),
]"""