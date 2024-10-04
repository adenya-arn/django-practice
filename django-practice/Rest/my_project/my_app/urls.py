from django.urls import path, include
from .views import BookListCreateAPIView, CohortViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cohorts', CohortViewSet, basename='cohort')


urlpatterns = [
    #path('', include(router.urls)),
    path('books/', BookListCreateAPIView.as_view(), name='book_list_create_view'),
]
urlpatterns += router.urls