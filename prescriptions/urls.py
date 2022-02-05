from django.urls import path
from .views import PrescriptionList, PrescriptionDetailView

urlpatterns = [
    path('', PrescriptionList.as_view()),
    path('<int:id>', PrescriptionDetailView.as_view()),
]