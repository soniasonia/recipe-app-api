from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe.views import TagViewSet, IngredientViewSet

# default router automatically registers URLs
# for all actions in the viewset

router = DefaultRouter()
router.register('tags', TagViewSet)
router.register('ingredients', IngredientViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
