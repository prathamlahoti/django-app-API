from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from posts.urls import router as posts_router
from categories.urls import router as categories_router
from tags.urls import router as tags_router
from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(title='Django app API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('schema/', schema_view),
    path('', include(posts_router.urls)),
    path('', include(categories_router.urls)),
    path('', include(tags_router.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
