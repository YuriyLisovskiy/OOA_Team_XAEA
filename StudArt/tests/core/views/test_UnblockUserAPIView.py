import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import force_authenticate
from rest_framework_simplejwt.state import User

from core.views import UnblockUserAPIView
from tests.common import APIFactoryTestCase


class UnblockUserAPITestCase(APIFactoryTestCase):
	def setUp(self) -> None:
		super(UnblockUserAPITestCase, self).setUp()
		self.view = UnblockUserAPIView.as_view()
		self.user = User.objects.get(username='User3')
	
	def test_Unblock(self):
		request = self.request_factory.put(reverse('api_v1:core:unblock_author'), {
			'author_pk': '1'
		})
		force_authenticate(request, self.user)
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
	
	def test_UnblockTwice(self):
		request = self.request_factory.put(reverse('api_v1:core:unblock_author'), {
			'author_pk': '1'
		})
		force_authenticate(request, self.user)
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
	
	def test_UnblockNonexistent(self):
		request = self.request_factory.put(reverse('api_v1:core:unblock_author'), {
			'author_pk': '9999'
		})
		force_authenticate(request, self.user)
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
	
	def test_UnblockUnauthenticated(self):
		request = self.request_factory.put(reverse('api_v1:core:unblock_author'), {
			'author_pk': '1'
		})
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
	
	def test_UnblockSelf(self):
		request = self.request_factory.put(reverse('api_v1:core:unblock_author'), {
			'author_pk': '3'
		})
		force_authenticate(request, self.user)
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
