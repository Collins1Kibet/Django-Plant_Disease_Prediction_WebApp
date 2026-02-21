from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('uploadimage', views.UploadImageViewset)

urlpatterns = [
    path('', views.upload_image_view, name='upload_image'),
    path('api/', include(router.urls)),
]