from .views_api.candidate import CandidateListApiView, CandidateRetrieveUpdateDestroyAPIView, CandidateRevApiView , CandidateRetrieveAPIView, CandidateFileApiView, ClientListApiView
from .views_api.weekly_hours import WeekHourView
from django.urls import include, path


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', WeekHourView)

urlpatterns = [
    path('', CandidateListApiView.as_view(), name=CandidateListApiView.name),
    path('contacts/', ClientListApiView.as_view(), name=ClientListApiView.name),
    path('<int:pk>/', CandidateRetrieveUpdateDestroyAPIView.as_view(), name=CandidateRetrieveUpdateDestroyAPIView.name),
    path('get-all-candidates/<int:page>/<str:name>', CandidateRetrieveAPIView.as_view(), name=CandidateListApiView.name),
    path('uploadingfile', CandidateFileApiView.as_view(), name=CandidateFileApiView.name),
    path('logs/', CandidateRevApiView.as_view(), name=CandidateRevApiView.name),
    path('weekhours/', include(router.urls)),
]
