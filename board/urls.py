# community/board/urls.py

from django.urls import path
from .views import PostListView, PostDetailView, CommentListView, CommentDetailView, FacilityListView, FacilityList

app_name = 'board'

urlpatterns = [
    path('load-json/', FacilityList.as_view(), name='load-json'),
    path('facilities/', FacilityListView.as_view(), name='facility_list'),
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:post_id>/comment/', CommentListView.as_view(), name='comment_list'),
    path('<int:post_id>/comment/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
]