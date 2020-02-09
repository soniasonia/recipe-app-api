from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe.views import TagViewSet

# default router automatically registers URLs
# for all actions in the viewset

router = DefaultRouter()
router.register('tags', TagViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
