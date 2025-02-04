from django.urls import path, include, re_path
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('blog.urls', namespace='blog')),
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
                       name='django.contrib.sitemaps.views.sitemap'),
                  path("accounts/", include("accounts.urls")),
                  path("accounts/", include("django.contrib.auth.urls")),
                  re_path(r'^oauth/', include('social_django.urls', namespace='social')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)