from django.shortcuts import render,redirect,HttpResponseRedirect
from Railwayticket.models import UserDetails
from django.shortcuts import render_to_response,HttpResponse
from django.views.generic import TemplateView
from django.views.generic import View

import os.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "train.db")

class TicketCreate(View):
    def get(self, request, *args, **kwargs):
        '''
        List all tickets
        :param request:
        :param args:
        :param kwargs:
        :return:List all tickets
        '''
        user_list = UserDetails.objects.all() # Getting user details
        return render(request, 'railwayreservation.html', {'result': user_list})

    def post(self, request, *args, **kwargs):
        '''
        Book tickets
        :param request: name,age,gender,berth perferences
        :param args:
        :param kwargs:
        :return: booked tickets
        '''
        check_waiting_list = UserDetails.objects.filter(status="Waiting List").count() # Getting user details with waiting list count
        if check_waiting_list <= 5:
            berth_per = request.POST.get('berth')
            list_count = UserDetails.objects.all().count()
            if list_count <= 8:
                coach = 'S1'
            elif list_count <= 16:
                coach = 'S2'
            elif list_count <= 24:
                coach = 'S3'
            elif list_count <= 32:
                coach = 'S4'
            else:
                coach = ''
            if request.POST.get('name')!= None:
                if list_count <= 24 and not request.POST.get('age') <= '5' :
                    if request.POST.get('age') >= '60':
                        berth_per = 'Lower'
                    status_text = 'Confirm'
                elif (list_count <= 32 and list_count > 24) or (request.POST.get('age') >= '60' and not request.POST.get('age') <= '5'):
                    if request.POST.get('age') >= '60':
                        berth_per = 'Lower'
                    status_text = 'RAC'
                elif (list_count <= 37 and list_count > 32) or (request.POST.get('age') >= '60'  and not request.POST.get('age') <= '5'):
                    if request.POST.get('age') >= '60':
                        berth_per = 'Lower'
                    status_text = 'Waiting List'
                else:
                    status_text = ''
                user_obj = UserDetails(name=request.POST.get('name'), age=request.POST.get('age'),
                                     Gender=request.POST.get('gender'), berth_perference=berth_per,
                                     status=status_text,coach=coach)
                user_obj.save()

            return HttpResponse("Your Ticket is Booked Successfully")
        else:
            return HttpResponse("No Tickets")

def cancel_ticket(request):
    '''
    Cancellation of ticket
    :param request:
    :return: Cancelled Ticket
    '''
    delete_obj = UserDetails.objects.filter(user_id=request.POST.get('delete_id')).delete() # delete all the ticket from database
    objj = UserDetails.objects.filter(status="Waiting List")
    for i in objj:
        update_rac_to_confirm = UserDetails.objects.filter(user_id=i.user_id).update(status='RAC')
    return render(request, 'railwayreservation.html', {'Cancel_resp': "Canceled"})

def booked_tickets(request):
    '''
    List the booked tickets and total number of ticket booked
    :param request:
    :return: booked tickets and count of booked tickets
    '''
    booked_ticket = UserDetails.objects.all()
    booked_ticket_count = UserDetails.objects.all().count()
    return render(request, 'view.html', {'posts': booked_ticket,'count':booked_ticket_count})

def unoccupied_tickets(request):
    '''
    List the Unoccupied tickets and total number of ticket unoccupied
    :param request:
    :return:  unoccupied tickets and count of unoccupied tickets
    '''
    unoccupied_ticket = UserDetails.objects.filter(status="Waiting List")
    unoccupied_ticket_count = UserDetails.objects.filter(status="Waiting List").count()
    return render(request, 'unoccupied_tickets.html', {'unoccupied': unoccupied_ticket,'count':unoccupied_ticket_count})




