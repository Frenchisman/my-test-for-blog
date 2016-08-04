"""test_zinnia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include  # , patterns
from django.conf.urls.static import static
from test_zinnia import settings
from django.contrib import admin
# from zinnia import urls as zinnia_urls
from django_comments import urls as django_comments_urls
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/', TemplateView.as_view(
        template_name='test_zinnia/about.html', name='about')),
    url(r'^galleries/', include('galleries.urls')),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include(django_comments_urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += patterns(
#         'django.views.static',
#         (r'media/(?P<path>.*)',
#             'serve',
#             {
#                 'document_root': settings.MEDIA_ROOT
#             }),
#     )
