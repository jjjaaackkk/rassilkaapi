from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LogoutView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)

from webui.views import (
    get_panel, get_campaigns, get_customers, get_messages, get_settings, get_login, login_page, save_settings
)
from api.views import (
    CampaignAPI1, CampaignAPI2, StatsAPI1, StatsAPI2, CustomerAPI1, CustomerAPI2, MessageAPI
)


favicon_view = RedirectView.as_view(url='/static/webui/img/favicon.ico', permanent=True)

# WebUI
urlpatterns = [
    re_path(r'^favicon\.ico$', favicon_view),
    path('', get_panel),
    path('admin/', admin.site.urls),
    re_path(r'^login', login_page),
    re_path(r'^logout', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    re_path(r'^post_login', get_login),
    path('account/campaigns/page/<int:page>', get_campaigns),
    re_path(r'^account/campaigns', get_campaigns),
    path('account/customers/page/<int:page>', get_campaigns),
    re_path(r'^account/customers', get_customers),
    re_path(r'^account/messages', get_messages),
    re_path(r'^account/settings', get_settings),
    re_path(r'^account', get_panel),
    re_path(r'^save_settings', save_settings),
]

# API 
urlpatterns += [
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/campaigns/<int:pk>', CampaignAPI2.as_view()),
    re_path('api/v1/campaigns', CampaignAPI1.as_view()),
    path('api/v1/customers/<int:pk>', CustomerAPI2.as_view()),
    re_path('api/v1/customers', CustomerAPI1.as_view()),
    path('api/v1/messages/<int:pk>', MessageAPI.as_view()),
    path('api/v1/stats/<int:pk>', StatsAPI2.as_view()),
    re_path('api/v1/stats', StatsAPI1.as_view()),
] 


# Swagger Docs
schema_view = get_schema_view(
   openapi.Info(
      title="Rassilka API",
      default_version='v1',
      description="Тестовое приложение Rassilki API",
      terms_of_service="",
      contact=openapi.Contact(email=""),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

#urlpatterns += doc_urls

urlpatterns += [
   path('docs(?<format>\json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

