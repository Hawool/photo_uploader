from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase, APIClient

from photos.base.services import create_image
from photos.models import Photo, UserModel


class PhotoModelTestCase(APITestCase):
    """testing methods: get, post"""

    def setUp(self):
        self.user = UserModel.objects.create(username='bob', password='bob')
        self.photo_1 = Photo.objects.create(owner=self.user, image='111.png')
        self.photo_2 = Photo.objects.create(owner=self.user, image='222.png')

        image = create_image(None, 'test.png')
        self.data = {"owner": self.user.id,
                     "image": SimpleUploadedFile('test.png', image.getvalue())}
        image_wrong = create_image(None, 'test_wrong.png', size=(10000, 10000))
        self.wrong_data = {"owner": self.user.id,
                           "image": SimpleUploadedFile('test_wrong.png', image_wrong.getvalue())}

        self.user = get_user_model().objects.create_user(username='sam', password='sam')
        self.authorized_client = APIClient()
        response = self.authorized_client.post('/auth/token/login/', {'username': 'sam', 'password': 'sam'})
        self.authorized_client.force_authenticate(self.user, response.data['auth_token'])

    def test_can_read_photos_list(self):
        """check get Photo list"""
        response = self.authorized_client.get('/api/v1/photos')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_photo(self):
        """check create Photo model"""
        url = '/api/v1/photos'
        response = self.authorized_client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cannot_create_photo(self):
        """check serializer validator for 200Kb"""
        url = '/api/v1/photos'
        response = self.authorized_client.post(url, self.wrong_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], [ErrorDetail(string='Image must be less 200Kb', code='invalid')])
