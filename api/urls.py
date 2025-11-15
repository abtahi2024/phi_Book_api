from django.urls import path,include
from rest_framework_nested import routers
from books.views import BookViewSet,CategoryViewSet,ReviewViewSet,BookImageViewSet
from order.views import CartViewSet,CartItemViewSet,OrderViewset

router=routers.DefaultRouter()
router.register('books',BookViewSet,basename='books')
router.register('categories',CategoryViewSet,basename='categories')
router.register('carts',CartViewSet,basename='carts')
router.register('orders',OrderViewset,basename='orders')

book_router=routers.NestedDefaultRouter(router,'books',lookup='book')
book_router.register('reviews',ReviewViewSet,basename='book-review')
book_router.register('images',BookImageViewSet,basename='book-images')

cart_router=routers.NestedDefaultRouter(router,'carts',lookup='cart')
cart_router.register('items',CartItemViewSet,basename='cart-item')
urlpatterns = [
    path('',include(router.urls)),
    path('',include(book_router.urls)),
    path('', include(cart_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
