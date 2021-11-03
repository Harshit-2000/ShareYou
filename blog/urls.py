from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name="home"),
    path('image/upload', views.upload_blog_view, name="upload_image"),
    path('blog/<int:id>', views.blog_view, name="view_blog"),
    path('blog/<int:id>/edit',
         views.edit_delete_view, name="edit_delete_blog"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
