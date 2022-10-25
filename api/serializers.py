from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    # below is to populate the owner field of Profile Model
    # using Profile Serializer
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)

    # this calls the get_all_reviews() as the name we have given is reviews -> both names should be same
    all_reviews = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"

    def get_all_reviews(self, obj):
        reviews = obj.review_set.all()
        sr = ReviewSerializer(reviews, many=True)
        return sr.data
