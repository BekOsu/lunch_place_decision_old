from rest_framework import generics
from .models import Vote
from .serializers import VoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import IsEmployee
from restaurants.models import Menu
from rest_framework import serializers, status
from django.utils import timezone
from django.db import models
from restaurants.serializers import MenuSerializer


class VoteCreateView(generics.CreateAPIView):
    serializer_class = VoteSerializer

    def post(self, request, *args, **kwargs):
        employee = request.user.employee
        menu_ids = request.data.get('menu_ids', [])
        points_list = request.data.get('points_list', [])

        if len(menu_ids) != len(points_list):
            return Response({'error': 'menu_ids and points_list must have the same length'},
                            status=status.HTTP_400_BAD_REQUEST)

        menu_queryset = Menu.objects.filter(id__in=menu_ids)
        if menu_queryset.count() != len(menu_ids):
            return Response({'error': 'invalid menu_ids'}, status=status.HTTP_400_BAD_REQUEST)

        vote_objs = []
        for menu_id, points in zip(menu_ids, points_list):
            vote_objs.append(Vote(employee=employee, menu_id=menu_id, points=points))

        Vote.objects.bulk_create(vote_objs)
        menu_queryset.update(points=menu_queryset.values('id').annotate(total_points=models.Sum('vote__points')))

        return Response({'success': 'votes created successfully'}, status=status.HTTP_201_CREATED)


class MenuListView(generics.ListAPIView):
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated, IsEmployee]

    def get_queryset(self):
        today = timezone.now().date()
        employee = self.request.user.employee
        menus = Menu.objects.filter(date=today)
        return menus.annotate(total_points=models.Sum('vote__points')).order_by('-total_points', '-created_at')

# When an employee votes for a menu, you can increment the points field accordingly. For example, in the new version of the API, employees can give points from 1 to 3 for their top three menus. You can create an API view to handle employee and update the points field:
# To display the menus sorted by points, you can create a view that retrieves the menus and orders them by points in descending order:
