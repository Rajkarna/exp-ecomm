from django.urls import path
from django.conf.urls import url
from .views import GetAllOrdersView, GetOrderDetailsView, CartAddView, AddOrderView

urlpatterns = [
    url(r'^add_cart/', CartAddView.as_view(), name='add_cart'),
    url(r'^orders/', GetAllOrdersView.as_view(), name='get_all_orders'),
    url(r'^order_list/$', GetOrderDetailsView.as_view(), name='order_details'),
    url(r'^add_order/$', AddOrderView.as_view(), name='add_order'),

]