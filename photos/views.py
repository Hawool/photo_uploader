from rest_framework import generics, permissions, status
from rest_framework.response import Response

from photos.models import Photo
from photos.serializers import PhotoSerializer


class PhotoListCreateView(generics.ListCreateAPIView):
    """view for create and get Photo model"""
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = []
        # checking files in request and save model
        for file in request.FILES:
            serializer = self.get_serializer(data={'image': request.FILES[file], 'owner': request.user.id})
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            data.append(serializer.data)
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
