from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework import status
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, OpenApiParameter


class SignUpApiView(APIView):
    """
    api description
    """
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


    def post(self, request):
        srz_data = UserSerializer(data=request.data)
        if srz_data.is_valid():
            user = User.objects.create_user(
                phone_number=srz_data.validated_data['phone_number'],
                username=srz_data.validated_data['username'],
                email=srz_data.validated_data.get('email', ''),
                password=srz_data.validated_data['password']
            )
            return Response({
                "phone_number": srz_data.data['phone_number'],
                "username": srz_data.data['username'],
                "email": srz_data.data['email'],
                "tokens":{
                    'access_token': str(AccessToken.for_user(user)),
                    'refresh_token': str(RefreshToken.for_user(user)),
                    }
                }, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

