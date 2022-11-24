from rest_framework import permissions, serializers
from rest_framework.viewsets import ModelViewSet

from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]
class UserViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UserSerializer