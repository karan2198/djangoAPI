from rest_framework import serializers

class RecommendationRequestSerializer(serializers.Serializer):
    search_terms = serializers.CharField(max_length=255)
    age = serializers.CharField(max_length=50)
    social_category = serializers.CharField(max_length=50)
    gender = serializers.CharField(max_length=10)
    domicile_of_tripura = serializers.CharField(max_length=1)
    num_recommendations = serializers.IntegerField(default=5)
