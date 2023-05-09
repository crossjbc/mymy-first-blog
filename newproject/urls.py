from django.urls import path,include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/',include('myapp.urls')),
    path('',include('rest_framework.urls'))
    
]
#from rest_framework_simplejwt.views import (
 #   TokenObtainPairView,
   # TokenRefreshView,
#)

#urlpatterns = [
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

#]