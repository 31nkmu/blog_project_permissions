from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.post import views

router = DefaultRouter()
router.register('', views.PostApiView)

urlpatterns = [
    # path('', views.PostApiView.as_view({'get': 'list',
    #                                     'post': 'create'})),
    path('', include(router.urls)),
]

urlpatterns += router.urls
