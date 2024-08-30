from django.urls import path,include
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register('products',views.ProductView)
router.register('designs',views.DesignView )
router.register('cart',views.CartView)


urlpatterns = [
    path('',include(router.urls))
]
