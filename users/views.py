from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from .models import Profile
from .permissions import CustomReadOnly

# from rest_framework.generics import get_object_or_404


# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer



class LoginView(generics.GenericAPIView): 
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        print('test',token)
        return Response({"token": token.key}, status=status.HTTP_200_OK)



class ProfileView(generics.RetrieveUpdateAPIView):       
    queryset = Profile.objects.all() 
    serializer_class = ProfileSerializer
    

    
    # def get(self, request, pk):
    #     profile = get_object_or_404(User,id=pk)
    #     serializer = ProfileSerializer(profile)
    #     return response(serailizer.data, status=status.HTTP_200_OK)
    

# class ProfileView(generics.GenericAPIView):
#     serializer_class = ProfileSerializer

#     def patch(self, request):
#         profile = Profile.objects.get(user=request.user)
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         data = serializer.validated_data
#         profile.nickname = data['nickname']
#         profile.position = data['position']
#         profile.subjects = data['subjects']
#         if request.data['image']:
#             profile.image = request.data['image']
#         profile.save()
#         return Response({"result": "ok"},
#                         status=status.HTTP_206_PARTIAL_CONTENT)

#     def get(self, request, pk):
#         profile = get_object_or_404(Profile, pk=pk)
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data, status=status.HTTP_200_OK)

