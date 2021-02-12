from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'pr', ProjectViewSet, basename='projects')
router.register(r'ct', ContactViewSet, basename='contact')
urlpatterns = router.urls
