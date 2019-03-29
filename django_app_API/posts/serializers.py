from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # Post author is a read only field
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'posted_date', 'category', 'tags')
