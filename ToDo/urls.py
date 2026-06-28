from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # مسیرهای آماده ورود، خروج و تغییر رمز
    path('accounts/', include('accounts.urls')), # ثبت نام
]