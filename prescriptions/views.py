from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Prescription
from .serializers import PrescriptionSerializer
from rest_framework import permissions


class PrescriptionList(ListCreateAPIView):

    serializer_class = PrescriptionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Prescription.objects.filter(owner=self.request.user)


class PrescriptionDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = PrescriptionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Prescription.objects.filter(owner=self.request.user)