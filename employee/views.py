from rest_framework import generics, status
from .models import Vote, Employee
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import EmployeeSerializer, VoteSerializer
from restaurants.models import Menu
from rest_framework.response import Response
from datetime import date
from UserAuth.permissions import IsEmployee


class EmployeeList(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [AllowAny]


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]


class VoteList(generics.CreateAPIView, generics.ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated, IsEmployee]

    def create(self, request, *args, **kwargs):

        version = self.kwargs.get('version')

        if version == "v1":
            return self.create_vote_v1(request)
        elif version == "v2":
            return self.create_vote_v2(request)
        else:
            return Response("Invalid API version", status=status.HTTP_400_BAD_REQUEST)

    def create_vote_v1(self, request):
        menu_id = request.data.get('menu')

        if menu_id is None:
            return Response("Please select one restaurant", status=status.HTTP_400_BAD_REQUEST)

        menu = Menu.objects.filter(id=menu_id).first()

        if not menu:
            return Response("Invalid menu selection", status=status.HTTP_400_BAD_REQUEST)

        employee = request.user.employee
        vote, created = Vote.objects.update_or_create(
            employee=employee, created_at__date=date.today(), menu=menu,
            defaults={'points': 3}
        )
        queryset = Vote.objects.filter(employee=employee, created_at__date=date.today())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def create_vote_v2(self, request):
        selected_menus = request.data

        employee = request.user.employee
        points = [3, 2, 1]

        for index, selection in enumerate(selected_menus):
            menu_id = selection.get('menu')
            menu = Menu.objects.filter(id=menu_id).first()

            if not menu:
                return Response(f"Invalid selection for restaurant {index + 1}", status=status.HTTP_400_BAD_REQUEST)
            vote, created = Vote.objects.update_or_create(
                employee=employee, created_at__date=date.today(), menu=menu,
                defaults={'points': points[index]}
            )

        queryset = Vote.objects.filter(employee=employee, created_at__date=date.today())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return Vote.objects.filter(created_at__date=date.today())
