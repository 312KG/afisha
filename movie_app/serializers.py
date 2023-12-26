from rest_framework import serializers
from .models import Director, Movie, Review, Genre, Tag


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text rating created_at'.split()

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    genre = GenreSerializer()
    tags = TagSerializer(many=True)
    class Meta:
        model = Movie
        fields = 'id reviews title description duration director genre tags tags_str_model genre_name'.split()
        # depth=1

class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    average_rating = serializers.SerializerMethodField()
    def get_average_rating(self, obj):
        total_rating = sum(review.rating for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if num_reviews > 0:
            return total_rating / num_reviews
        else:
            return 0.0

    class Meta:
        model = Movie
        fields = 'title reviews average_rating'.split()
        # depth=1
