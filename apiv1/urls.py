from django.urls import include, path
from rest_framework import routers

from . import views

# routerを定義
router = routers.DefaultRouter()
router.register("reading_list", views.ReadingListViewSet)
router.register("reviews", views.ReviewViewSet)
router.register("categories", views.CategoryViewSet)

app_name = "apiv1"
urlpatterns = [
    path("", include(router.urls)),
]
