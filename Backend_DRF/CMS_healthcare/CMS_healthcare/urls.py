
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from CMS_patient_registration.views import PersonalViewSet, AddressDetailsViewSet, ContactDetailsViewSet
from CMS_scheduling.views import ServiceProviderViewSet, RoomCategoryViewSet
# from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

router = DefaultRouter()
router.register('personal', PersonalViewSet, basename='personal')
router.register('address', AddressDetailsViewSet, basename='address')
router.register('contact', ContactDetailsViewSet, basename='contact')
router.register('serviceprovider', ServiceProviderViewSet, basename='serviceprovider')
router.register('room', RoomCategoryViewSet, basename='room')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('registration/', include('CMS_patient_registration.urls')),
    # path('scheduling/', include('CMS_scheduling.urls')),
    # # path('access/', token_obtain_pair),
    # path('refresh/', token_refresh),
]
