from django.urls import path
from . import views
from Railwayticket.views import TicketCreate,AboutView
urlpatterns = [
    path('about/', AboutView.as_view()),
    path('', TicketCreate.as_view(), name='ticket'),
    path('cancel/', views.cancel_ticket, name='cancel'),
    path('print/', views.booked_tickets, name='print'),
    path('unoccupied/', views.unoccupied_tickets, name='unoccupied')
]