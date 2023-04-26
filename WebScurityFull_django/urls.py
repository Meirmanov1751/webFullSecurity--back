from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
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

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)