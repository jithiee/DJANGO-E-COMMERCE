
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  
    path('',views.home,name='home'),
    path('view/<int:car_id>/',views.viewdetiles,name='view'),
  
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #for its include media url
