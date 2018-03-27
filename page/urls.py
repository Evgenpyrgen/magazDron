from django.urls import  path, re_path
#from page import views
from page.twviews import GoodListView, GoodDetailView
from page.twviews import GoodCreate, GoodUpdate, GoodDelete


urlpatterns = [
    
    re_path(r'^$', GoodListView.as_view(), name = "index"),
    re_path(r'^(?:(?P<cat_id>\d+)/)?$', GoodListView.as_view(), name = "index"),
    re_path(r'^good/(?P<good_id>\d+)/$', GoodDetailView.as_view(), name = "good"),
    re_path(r'^(?P<cat_id>\d+)/add/$', GoodCreate.as_view(), name='good_add'),
    re_path(r'^good/(?P<good_id>\d+)/edit/$', GoodUpdate.as_view(), name='good_edit'),
    re_path(r'^good/(?P<good_id>\d+)/delete/$', GoodDelete.as_view(), name='good_delete'),
]
"""
urlpatterns = [
    #path("", GoodListView.as_view(), name = "index"),
    #path("<int:cat_id>/", GoodListView.as_view(), name = "index"),
    #path("good/<int:good_id>/", GoodDetailView.as_view(), name = "good"),
    #path('<int:cat_id>/add/', GoodCreate.as_view(), name='good_add'),
    #path('good/<int:good_id>/edit/', GoodUpdate.as_view(), name='good_edit'),
    #path('good/<int:good_id>/delete/', GoodDelete.as_view(), name='good_delete'),
]"""