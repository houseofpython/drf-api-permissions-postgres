from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Thing
from .serializer import ThingSerializer
from .permissions import isOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class ThingList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


# Create your views here.
