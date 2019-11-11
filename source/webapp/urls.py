from django.urls import path
from .views import IndexView, ProductView, ProductCreateView, BasketChangeView, BasketView, SessionStatsView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/<int:pk>/', ProductView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('basket/change/', BasketChangeView.as_view(), name='basket_change'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('session_stats/', SessionStatsView.as_view(), name='session_stats'),
]
