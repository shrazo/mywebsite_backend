"""
URL configuration for mywebsite_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter 
from mainapp.views import * 

router = DefaultRouter()
router.register(r'about', AboutViewSet, basename='about_viewset')
router.register(r'link', LinkViewSet, basename='link_viewset')
router.register(r'research', ResearchViewSet, basename='research_viewset')
router.register(r'publication', PublicationViewSet, basename='publication_viewset')
router.register(r'highlight', HighlightViewSet, basename='highlight_viewset')
router.register(r'experience', ExperienceViewSet, basename='experience_viewset')
router.register(r'education', EducationViewSet, basename='education_viewset')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
