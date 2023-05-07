from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import redirect, render
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from post.urls import router as post_router
from product.urls import router as product_router
from customer.urls import router as customer_router
from employee.urls import router as employee_router
from order.urls import router as order_router

router = DefaultRouter()

router.registry.extend(post_router.registry)
router.registry.extend(product_router.registry)
router.registry.extend(customer_router.registry)
router.registry.extend(employee_router.registry)
router.registry.extend(order_router.registry)

def base(request):
    return render(request, 'base.html')

urlpatterns = [
    path('', base),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)