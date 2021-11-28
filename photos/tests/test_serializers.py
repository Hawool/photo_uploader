from django.core.files.uploadedfile import SimpleUploadedFile

from photos.base.services import create_image
from photos.models import Photo, UserModel
from photos.serializers import PhotoSerializer
from rest_framework.test import APITestCase


class PhotoSerializerTestCase(APITestCase):
    """test for Photo serializer"""

    def setUp(self):
        self.user = UserModel.objects.create(username='cat', password='cat')
        image_1 = create_image(None, 'test_1.png')
        image_2 = create_image(None, 'test_2.png')
        self.photo_1 = Photo.objects.create(owner=self.user,
                                            image=SimpleUploadedFile('test.png', image_1.getvalue())
                                            )
        self.photo_2 = Photo.objects.create(owner=self.user,
                                            image=SimpleUploadedFile('test_2.png', image_2.getvalue())
                                            )

    def test_PhotoSerializer(self):
        data = PhotoSerializer([self.photo_1, self.photo_2], many=True).data
        expected_data = [
            {
                "owner": self.user.id,
                "image": f'/media/{self.photo_1.image}',
            },
            {
                "owner": self.user.id,
                "image": f'/media/{self.photo_2.image}',
            }
        ]
        self.assertEqual(expected_data, data)

