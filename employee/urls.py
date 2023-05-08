from .views import (
    EmployeeList,
    EmployeeDetail,
    VoteList,
)
from django.urls import path

urlpatterns = [
    # employees
    path('account', EmployeeList.as_view(), name='employee_List'),
    path('account/<int:pk>/', EmployeeDetail.as_view(), name='employee_detail'),
    # voting
    path('votes/<str:version>/', VoteList.as_view(), name='vote_list'),
    path('votes/<str:version>/', VoteList.as_view(), name='vote_list'),
]
