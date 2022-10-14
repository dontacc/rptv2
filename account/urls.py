from account import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('customer', views.CustomerViewSet)
router.register('order', views.OrderViewSet)

urlpatterns =router.urls
