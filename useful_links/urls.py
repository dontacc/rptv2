from . import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('contact_us', views.Questions)
router.register('collection', views.CollectionModelViewSet)

urlpatterns =router.urls