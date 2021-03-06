import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import force_authenticate
from rest_framework_simplejwt.state import User

from artwork.views.artwork import ArtworksAPIView
from tests.common import APIFactoryTestCase


class ArtworksAPITestCase(APIFactoryTestCase):
	def setUp(self) -> None:
		super(ArtworksAPITestCase, self).setUp()
		self.view = ArtworksAPIView.as_view()
		self.user_4 = User.objects.get(username='User4')
		self.user_user = User.objects.get(username='User')

	def test_getArtworksTwoColumnsFirstPage(self):
		request = self.request_factory.get(reverse('api_v1:artwork:get_artworks'), {'columns': 2, 'page': 1})
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['count'], 22)
		self.assertEqual(len(response.data['results']), 2)

	def test_getArtworksTwoColumnsFirstPage(self):
		request = self.request_factory.get(reverse('api_v1:artwork:get_artworks'), {'columns': 2, 'page': 1})
		force_authenticate(request, self.user_user)
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['count'], 22)
		self.assertEqual(len(response.data['results']), 2)

	def test_getArtworksFourColumnsFirstPage(self):
		request = self.request_factory.get(reverse('api_v1:artwork:get_artworks'), {'columns': 4, 'page': 1})
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['count'], 22)
		self.assertEqual(len(response.data['results']), 4)

	def test_getArtworksFourColumnsSecondPage(self):
		request = self.request_factory.get(reverse('api_v1:artwork:get_artworks'), {'columns': 4, 'page': 2})
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['count'], 22)
		self.assertEqual(len(response.data['results']), 4)

	def test_getArtworksOutOfBoundsPage(self):
		request = self.request_factory.get(reverse('api_v1:artwork:get_artworks'), {'columns': 3, 'page': 5})
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_getArtworksFilterByTagFirstPage(self):
		request = self.request_factory.get(reverse('api_v1:artwork:get_artworks'), {'columns': 3, 'page': 1, 'tag': 'tag1'})
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['count'], 11)
		self.assertEqual(len(response.data['results']), 3)

	def test_getArtworksFilterByTagLastPage(self):
		request = self.request_factory.get(reverse('api_v1:artwork:get_artworks'), {'columns': 3, 'page': 2, 'tag': 'tag1'})
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['count'], 11)
		self.assertEqual(len(response.data['results']), 3)
		self.assertEqual(len(response.data['results'][0]), 2)
		self.assertEqual(len(response.data['results'][1]), 2)
		self.assertEqual(len(response.data['results'][2]), 1)

	def test_getArtworksFilterByAuthorFirstPage(self):
		request = self.request_factory.get(reverse('api_v1:artwork:get_artworks'), {'columns': 3, 'page': 1, 'author': 'User2'})
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['count'], 16)
		self.assertEqual(len(response.data['results']), 3)

	def test_getArtworksFilterByAuthorLastPage(self):
		request = self.request_factory.get(reverse('api_v1:artwork:get_artworks'), {'columns': 3, 'page': 3, 'author': 'User2'})
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['count'], 16)
		self.assertEqual(len(response.data['results']), 3)
		self.assertEqual(len(response.data['results'][0]), 2)
		self.assertEqual(len(response.data['results'][1]), 1)
		self.assertEqual(len(response.data['results'][2]), 1)

# todo: test filter_by_subscriptions

	def test_getArtworksFilterTrue(self):
		request = self.request_factory.get(reverse('api_v1:artwork:get_artworks'), {'columns': 3, 'page': 1, 'filter_by_subscriptions': True})
		force_authenticate(request, user=self.user_4)
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['count'], 6)

	def test_getArtworksFilterTrueNoSubs(self):
		request = self.request_factory.get(reverse('api_v1:artwork:get_artworks'), {'columns': 3, 'page': 1, 'filter_by_subscriptions': True})
		force_authenticate(request, user=self.user_user)
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['count'], 0)

	def test_getArtworksFilterTrueUnauthenticated(self):
		request = self.request_factory.get(reverse('api_v1:artwork:get_artworks'), {'columns': 3, 'page': 1, 'filter_by_subscriptions': True})
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

