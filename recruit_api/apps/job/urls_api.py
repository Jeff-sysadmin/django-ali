from django.conf.urls import url
from .views_api.job import JobView
from rest_framework.routers import DefaultRouter
from django.urls import include, path

router = DefaultRouter()
router.register('', JobView)

urlpatterns = [
        path('', include(router.urls)),
]
