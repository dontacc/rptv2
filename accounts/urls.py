from accounts import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('customer', views.CustomerViewSet)
router.register('order', views.OrderViewSet,basename='order')
urlpatterns =router.urls
