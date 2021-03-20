from BookStore.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BookViewSet, basename='books')
router.register(r'', JournalViewSet, basename='journals')
urlpatterns = router.urls