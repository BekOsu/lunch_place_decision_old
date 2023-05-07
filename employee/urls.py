from .views import (
    EmployeeList,
    EmployeeDetail,
    VoteCreateView,
    MenuListView
)
from django.urls import path

urlpatterns = [
    # employees
    path('employees/', EmployeeList.as_view(), name='employee_List'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee_detail'),
    # voting
    path('vote-create/', VoteCreateView.as_view(), name='vote_create'),
    path('voted-list/', MenuListView.as_view(), name='vote_create'),
]
