from django.urls import path
from . views import Index, beforecontent,createreserve,calendar_A,calendar_B,calendar_C,reserve,Delete

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('create/',createreserve.as_view(),name='create'),
    path('room_A/',calendar_A,name='room_A'),
    path('room_B/',calendar_B,name='room_B'),
    path('room_C/',calendar_C,name='room_C'),
    path('<int:pk>/before/',beforecontent,name='before'),
    path('reserve/',reserve,name='reserve'),
    path('<int:pk>/Delete/',Delete.as_view(),name='Delete'),
]