from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RecommendationRequestSerializer
from .models import get_recommendations

@api_view(['POST'])
def recommend(request):
    serializer = RecommendationRequestSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        recommendations = get_recommendations(
            data['search_terms'],
            data['age'],
            data['social_category'],
            data['gender'],
            data['domicile_of_tripura'],
            data['num_recommendations']
        )
        return Response({'recommendations': recommendations}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
