from rest_framework import generics
from .models import Vote
from .serializers import VoteSerializer
from .permissions import IsEmployee


class VoteCreateView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsEmployee]

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user.employee)
