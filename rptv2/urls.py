"""rptv2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken import views
from dj_rest_auth.views import PasswordResetConfirmView,PasswordResetView
from message.views import *
from core.views import ActivationView,AddPhoneView
schema_view = get_schema_view(
   openapi.Info(
      title="rptv2 API",
      default_version='v1',
      description="here is all our endpoints",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="GPv3 License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('movies.urls')),
    path('useful_links/',include('useful_links.urls')),
    path('user/', include('accounts.urls')),
    path('match/', include('match.urls')),
    path('send_otp/',send_otp),
    path('__debug__/', include('debug_toolbar.urls')),


    path('DjRestAuth/', include('dj_rest_auth.urls')),
    path('DjRestAuth/registration/', include('dj_rest_auth.registration.urls')),
    path('DjRestAuth/registration/addphone', AddPhoneView.as_view()),
    path('DjRestAuth/registration/activation', ActivationView.as_view()),
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('DjRestAuth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('token/', views.obtain_auth_token),


    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)