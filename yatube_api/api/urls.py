from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'
router = DefaultRouter()
router1 = DefaultRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')
router1.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/jwt/create/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/jwt/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('v1/jwt/verify/', jwt_views.TokenVerifyView.as_view(),
         name='token_verify'),
    path('v1/', include(router.urls)),
    path('v1/posts/<int:post_id>/', include(router1.urls)),
]
