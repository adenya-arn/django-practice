from django.urls import path

from .views import (
    ArticleCreateView,
    ArticleDeleteView,
    ArticleDetailtView,
    ArticleListView,
    ArticleUpdateView,
)
app_name = 'articles'


"""urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    #path('create/', view_name, name='article-create'),
    path('<int:id>/', ArticleDetailView, name='article-detail'),
    #path('<int:id>/update/', view_name, name='article-update'),
    #path('<int:id>/delete/', view_name, name='article-delete'),
]"""

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/', ArticleDetailtView.as_view(), name='article-detail'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    #path('<int:id>/delete/', view_name, name='article-delete'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]