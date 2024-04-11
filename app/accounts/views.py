from .models import profile
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle


class UserList(generics.ListAPIView):
    model = profile
    queryset = profile.objects.all()
    serializer_class = currentUserSerializer
    throttle_classes = [UserRateThrottle]
    #permission_classes = [IsAuthenticated]

    def list(self,req):
        #print(self.request.query_params)
        #print(self.request.user)
        return super(UserList,self).list(req)
