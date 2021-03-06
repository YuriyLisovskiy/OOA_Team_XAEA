import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import force_authenticate
from rest_framework_simplejwt.state import User

from artwork.views.comment import EditCommentAPIView
from tests.common import APIFactoryTestCase


class EditCommentAPITestCase(APIFactoryTestCase):
	def setUp(self) -> None:
		super(EditCommentAPITestCase, self).setUp()
		self.view = EditCommentAPIView.as_view()
		self.user_olivia = User.objects.create_user(username='olivia', password='StrongPassword12345')
		self.user_user = User.objects.get(username='User', email='mail@mail.com')

	def test_EditComment(self):
		request = self.request_factory.put(reverse('api_v1:artwork:edit_comment', args=[16]), json.dumps({"text": "New text"}), content_type="application/json")
		force_authenticate(request, user=self.user_user)
		response = self.view(request, pk=16)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_EditCommentUnauthenticated(self):
		request = self.request_factory.put(reverse('api_v1:artwork:edit_comment', args=[16]), json.dumps({"text": 'New text'}), content_type='application/json')
		response = self.view(request, pk=16)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_EditCommentWithReplies(self):
		request = self.request_factory.put(reverse('api_v1:artwork:edit_comment', args=[1]), json.dumps({"text": 'New text'}), content_type='application/json')
		force_authenticate(request, user=self.user_user)
		response = self.view(request, pk=1)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_EditNonexistentComment(self):
		request = self.request_factory.put(reverse('api_v1:artwork:edit_comment', args=[9999]), {"text": 'New text'}, content_type='application/json')
		force_authenticate(request, user=self.user_user)
		response = self.view(request, pk=9999)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_EditNotYourComment(self):
		request = self.request_factory.put(reverse('api_v1:artwork:edit_comment', args=[16]), {"text": 'New text'}, content_type='application/json')
		force_authenticate(request, user=self.user_olivia)
		response = self.view(request, pk=16)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
