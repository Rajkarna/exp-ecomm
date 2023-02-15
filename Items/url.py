from django.urls import path
from django.conf.urls import url
from Items.views import GetAllItemsView,GetItemDetailsView,ItemAddView,AddRatingView,GetAvgRatingView,\
GetItemReviewsView,UserCountAPI


urlpatterns = [
    url(r'^items/', GetAllItemsView.as_view(), name='get_all_items'),
    url(r'^items/$', GetItemDetailsView.as_view(), name='get_item_details'),
    url(r'^add_items/$', ItemAddView.as_view(), name='add_items'),
    url(r'^add_rating/$', AddRatingView.as_view(), name='add_rating'),
    url(r'^avg_rating/$', GetAvgRatingView.as_view(), name='avg_rating'),
    url(r'^get_reviews/$', GetItemReviewsView.as_view(), name='get_review'),
    url(r'^add_user_count/$', UserCountAPI.as_view(), name='user-count'),

]