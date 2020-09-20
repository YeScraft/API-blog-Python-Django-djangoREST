from .models import Post, Category
from rest_framework import serializers
from django.contrib.auth.models import User


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'status', 'content', 'category']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class PostSerializer(serializers.ModelSerializer):

    # author = AuthorSerializer(required=False)
    # category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


# class AuthorPostSerializer(serializers.ModelSerializer):
#
#     first_name = serializers.CharField(read_only=True, source='User__first_name')
#     last_name = serializers.CharField(read_only=True, source='User__last_name')
#
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name']


class CategoryPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['title']


# class PostSerializer(serializers.ModelSerializer):
#
#     author_name = serializers.CharField(source='author.username', read_only=True)
#     author_id = serializers.IntegerField(source='author.id')
#     # category = CategoryPostSerializer(required=False)
#     category = serializers.CharField(source='category.title')
#     # author = AuthorPostSerializer(required=False)

    # def create(self, validated_data):
    #     author_id = validated_data.pop('author', {}).pop('id', None)
    #     category_title = validated_data.pop('category', {}).pop('title', None)
    #     if not author_id:
    #         raise Exception('Incorrect author id')
    #     try:
    #         author = User.objects.get(id=author_id)
    #         category, created = Category.objects.get_or_create(title=category_title)
    #     except User.DoesNotExist:
    #         raise Exception('User does not exist')
    #     return Post.objects.create(author=author, category=category, **validated_data)
    #
    # class Meta:
    #     model = Post
    #     fields = ['title', 'status', 'content', 'updated', 'publication_date', 'author_id', 'author_name', 'category']


class PostDetailSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    # post = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)
    posts = PostDetailSerializer(many=True, required=False)

    class Meta:
        model = Category
        # fields = ['title', 'posts']
        fields = '__all__'

