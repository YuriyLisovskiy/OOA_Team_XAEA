from django.urls import re_path

from artwork.views import (
	ArtworksAPIView, ArtworkAPIView, VoteForArtworkAPIView,
	VoteForCommentAPIView, CommentAPIView, CommentsAPIView
)

app_name = 'artwork'

urlpatterns = [
	re_path(r'^comments/(?P<pk>\d+)/vote/?$', VoteForCommentAPIView.as_view()),
	re_path(r'^comments/(?P<pk>\d+)/?$', CommentAPIView.as_view()),
	re_path(r'^comments/?$', CommentsAPIView.as_view()),
	re_path(r'^(?P<pk>\d+)/vote/?$', VoteForArtworkAPIView.as_view()),
	re_path(r'^(?P<pk>\d+)/?$', ArtworkAPIView.as_view()),
	re_path(r'^$', ArtworksAPIView.as_view())
]