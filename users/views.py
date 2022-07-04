from rest_framework.views import APIView
from rest_framework import  status
from rest_framework.response import Response

from users.serializers import UserSignupSerializer
from users.jwt_claim_serializer import SpartaTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class UserView(APIView):

    # 사용자 정보 조회
    def get(self, request):
        return Response(UserSignupSerializer(request.user).data, status=status.HTTP_200_OK)

    # 회원가입
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입 완료!!"})
        else:
            return Response({"message": f'${serializer.errors}'}, 400)

    # 회원 정보 수정
    def put(self, request):
        return Response({"message": "put method!!"})

    # 회원 탈퇴
    def delete(self, request):
        return Response({"message": "delete method!!"})



class SpartaTokenObtainPairView(TokenObtainPairView):
    serializer_class = SpartaTokenObtainPairSerializer