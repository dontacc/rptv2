from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Q&A', views.QandASupportModelViewSet)
router.register('refund_policy', views.RefundPolicyModelViewSet)
router.register('contact', views.ContactModelViewSet)
router.register('privacy_policy', views.PrivacyPolicyViewSet)

urlpatterns = router.urls
