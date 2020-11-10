from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.response import Response

from auth.serializers import UserWithTokenSerializer


# /api/v1/auth/register
# methods:
#   - post: username, email, password
from core.models import User


class RegisterUserAPIView(generics.CreateAPIView):
	permission_classes = (permissions.AllowAny,)
	serializer_class = UserWithTokenSerializer


# /api/v1/auth/userExists
# methods:
#   - get: username, email
class UserExistsAPIView(generics.RetrieveAPIView):
	permission_classes = (permissions.AllowAny,)

	def get(self, request, *args, **kwargs):
		q = None
		username = request.GET.get('username', None)
		if username:
			q = Q(username=username)

		email = request.GET.get('email', None)
		if email:
			email_q = Q(email=email)
			if q:
				q |= email_q
			else:
				q = email_q

		data = dict()
		if q:
			exists = User.objects.filter(q).exists()
			data['exists'] = exists
			if exists:
				data['message'] = 'User with this username and(or) email address already exists'

			return Response(data)
		else:
			return Response(status=400)