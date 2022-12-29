from django.urls import re_path
from rest_framework import routers
from .views import GetAllServiceView,ServiceViewSet_v1, ServiceViewSet


router=routers.DefaultRouter()
router.register(r'v1/service', ServiceViewSet_v1)
router.register(r'v2/service', ServiceViewSet)

urlpatterns=[
    re_path(r'v2/service',GetAllServiceView.as_view()),
]

urlpatterns += router.urls