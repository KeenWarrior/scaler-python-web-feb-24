from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models import Group
from ..serializers import GroupSerializer


class GroupListCreateAPIView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
