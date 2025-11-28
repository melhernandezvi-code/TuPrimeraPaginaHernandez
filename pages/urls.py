from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('crear/', PostCreateView.as_view(), name='post-create'),
    path('editar/<int:pk>/', PostUpdateView.as_view(), name='post-edit'),
    path('borrar/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('', views.page_list, name='page_list'),
    path('<int:pk>/', views.page_detail, name='page_detail'),
]
