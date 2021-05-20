from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from cars import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('inventory/', views.inventory, name="inventory"),
    path('dealers/', views.dealers, name="dealers"),
    path('contact/', views.contact, name="contact"),
    path('filter_results/', views.filter_results, name="filter_results"),
    path('<int:car_id>/', views.car_detail, name="car_detail"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
