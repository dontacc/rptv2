from . import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('viewer', views.VeiwerFormViewSet)
router.register('participate', views.ParticipateFormViewSet)

urlpatterns =router.urls