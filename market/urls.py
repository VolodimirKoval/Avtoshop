from django.urls import path
from market.views import goods, basket_add, basket_remove, index

app_name = 'market'

urlpatterns = [
    path('category<int:category_id>/', index, name='category'),
    path('page/<int:page_number>/', index, name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),

]