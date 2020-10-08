"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

#import ipdb; ipdb.set_trace()

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

    path('', include(('cride.circles.urls', 'circles'), namespace='circles')),
    path('', include(('cride.users.urls', 'users'), namespace='users')),
    path('', include(('cride.rides.urls', 'rides'), namespace='rides')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
