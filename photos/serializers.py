from rest_framework import serializers

from photos.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    """Serializer for Photo model"""
    class Meta:
        model = Photo
        fields = ['image', 'owner']

    def validate(self, attrs):
        # except id size of image is over 200Kb
        if attrs['image'].size >= 200000:
            raise serializers.ValidationError({'error': 'Image must be less 200Kb'})
        return attrs
