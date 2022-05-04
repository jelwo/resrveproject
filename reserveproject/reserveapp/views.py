from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import FormView,CreateView,DeleteView
from . import forms
from .models import reservemodel2
from django.urls import reverse_lazy,reverse
import pandas as pd
import datetime
from bootstrap_datepicker_plus.widgets import DatePickerInput,TimePickerInput
from django.template import loader
from urllib.parse import urlencode


posted_data = {
    "checkin": "",
    "time1": "",
    "checkout": "",
    "time2": "",
}

availableroom=['A室','B室','C室']

#----------------------------------------Create---------------------------------------------
class Index(FormView):
    form_class = forms.inputdialog
    template_name = 'index.html'
    success_url = reverse_lazy('create')
    
    def get_form(self):
        form = super().get_form()
        form.fields['checkin'].widget = DatePickerInput(format='%Y-%m-%d')
        form.fields['checkout'].widget = DatePickerInput(format='%Y-%m-%d')
        form.fields['time1'].widget = TimePickerInput()
        form.fields['time2'].widget = TimePickerInput()
        return form

    def form_valid(self, form):
        posted_data['checkin'] = form.data.get('checkin')
        posted_data['time1'] = form.data.get('time1')
        posted_data['checkout'] = form.data.get('checkout')
        posted_data['time2'] = form.data.get('time2')
        arrinputcheckin=posted_data['checkin'].split('-')
        arrinputcheckout=posted_data['checkout'].split('-')
        arrinputtime1=posted_data['time1'].split(':')
        arrinputtime2=posted_data['time2'].split(':')
        try:
            df = pd.DataFrame(list(reservemodel2.objects.all().values()))   
            for date in df.itertuples():
                dfcheckin=date.checkin
                arrcheckin=dfcheckin.split('-')
                dfcheckout=date.checkout
                arrcheckout=dfcheckout.split('-')
                dftime1=date.time1
                arrtime1=dftime1.split(':')
                dftime2=date.time2
                arrtime2=dftime2.split(':')
                if datetime.datetime(int(arrcheckin[0]),int(arrcheckin[1]),int(arrcheckin[2]),int(arrtime1[0]),int(arrtime1[1])) <= datetime.datetime(int(arrinputcheckin[0]),int(arrinputcheckin[1]),int(arrinputcheckin[2]),int(arrinputtime1[0]),int(arrinputtime1[1])) <= datetime.datetime(int(arrcheckout[0]),int(arrcheckout[1]),int(arrcheckout[2]),int(arrtime2[0]),int(arrtime2[1])) or datetime.datetime(int(arrcheckin[0]),int(arrcheckin[1]),int(arrcheckin[2]),int(arrtime1[0]),int(arrtime1[1])) <= datetime.datetime(int(arrinputcheckout[0]),int(arrinputcheckout[1]),int(arrinputcheckout[2]),int(arrinputtime2[0]),int(arrinputtime2[1])) <= datetime.datetime(int(arrcheckout[0]),int(arrcheckout[1]),int(arrcheckout[2]),int(arrtime2[0]),int(arrtime2[1])):
                    try:
                        room=date.category
                        availableroom.remove(room)
                    except:
                        continue      
        except:
            pass
        return super().form_valid(form)
        
class createreserve(CreateView):
    model = reservemodel2
    template_name = 'createreserve.html'
    fields = ['checkin','time1','checkout','time2','category']
    success_url = reverse_lazy('reserve')
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['category']=availableroom
        return context 

    def get_initial(self):
          initial = super().get_initial()
          initial['checkin'] = posted_data['checkin']
          initial['time1'] = posted_data['time1']
          initial['checkout'] = posted_data['checkout']
          initial['time2'] = posted_data['time2']
          return initial
#-----------------------------------------------------------------------------------------

#---------------------------------------Update--------------------------------------------
posted_data2 = {
    "checkin": "",
    "time1": "",
    "checkout": "",
    "time2": "",
    "id": "",
}

availableroom2=['A室','B室','C室']

def beforecontent(request,pk):
    if request.method == 'POST':
        if 'changebtn' in request.POST: #遷移先で変更ボタンが押された場合
            db = reservemodel2.objects.get(pk=pk)
            db.checkin = request.POST['checkin']
            db.time1 = request.POST['time1']
            db.checkout = request.POST['checkout']
            db.time2 = request.POST['time2']
            db.category = request.POST['category']
            db.save()
            return render(request,'result.html')
        else: #遷移前に検索ボタンが押された場合
            form = forms.inputdialog(
                initial={
                    'checkin':request.POST['checkin'],
                    'time1':request.POST['time1'],
                    'checkout':request.POST['checkout'],
                    'time2':request.POST['time2'],
                    }
                )
            object = reservemodel2.objects.get(pk=pk)
            posted_data2['checkin'] = request.POST['checkin']
            posted_data2['time1'] = request.POST['time1']
            posted_data2['checkout'] = request.POST['checkout']
            posted_data2['time2'] = request.POST['time2']
            posted_data2['id'] = object.id
            arrinputcheckin=posted_data2['checkin'].split('-')
            arrinputcheckout=posted_data2['checkout'].split('-')
            arrinputtime1=posted_data2['time1'].split(':')
            arrinputtime2=posted_data2['time2'].split(':')
            try:
                df = pd.DataFrame(list(reservemodel2.objects.all().values()))
                newdf=df[df['id'] != posted_data2['id']]
                for date in newdf.itertuples():
                    dfcheckin=date.checkin
                    arrcheckin=dfcheckin.split('-')
                    dfcheckout=date.checkout
                    arrcheckout=dfcheckout.split('-')
                    dftime1=date.time1
                    arrtime1=dftime1.split(':')
                    dftime2=date.time2
                    arrtime2=dftime2.split(':')
                    if datetime.datetime(int(arrcheckin[0]),int(arrcheckin[1]),int(arrcheckin[2]),int(arrtime1[0]),int(arrtime1[1])) <= datetime.datetime(int(arrinputcheckin[0]),int(arrinputcheckin[1]),int(arrinputcheckin[2]),int(arrinputtime1[0]),int(arrinputtime1[1])) <= datetime.datetime(int(arrcheckout[0]),int(arrcheckout[1]),int(arrcheckout[2]),int(arrtime2[0]),int(arrtime2[1])) or datetime.datetime(int(arrcheckin[0]),int(arrcheckin[1]),int(arrcheckin[2]),int(arrtime1[0]),int(arrtime1[1])) <= datetime.datetime(int(arrinputcheckout[0]),int(arrinputcheckout[1]),int(arrinputcheckout[2]),int(arrinputtime2[0]),int(arrinputtime2[1])) <= datetime.datetime(int(arrcheckout[0]),int(arrcheckout[1]),int(arrcheckout[2]),int(arrtime2[0]),int(arrtime2[1])):
                        try:
                            room=date.category
                            availableroom2.remove(room)
                        except:
                            continue      
            except:
                pass            
            return render(request,'changereserve.html',{"form": form,"pk": pk,"room":availableroom2})
    else: #GET通信
        object = reservemodel2.objects.get(pk=pk)
        form = forms.inputdialog(
            initial={
                'checkin':object.checkin,
                'time1':object.time1,
                'checkout':object.checkout,
                'time2':object.time2,
                }
            )
        form.fields['checkin'].widget = DatePickerInput(format='%Y-%m-%d')
        form.fields['checkout'].widget = DatePickerInput(format='%Y-%m-%d')
        form.fields['time1'].widget = TimePickerInput()
        form.fields['time2'].widget = TimePickerInput()
        return render(request,'changeindex.html',{"form": form,"pk": pk})
#----------------------------------------------------------------------------------------------------

def calendar_A(request):
    querydf=reservemodel2.objects.filter(category='A室')
    context = {
   'df_A' : querydf, 
 }
    return render(request, 'calendar_A.html', context)

def calendar_B(request):
    querydf=reservemodel2.objects.filter(category='B室')
    context = {
   'df_B' : querydf, 
 }
    return render(request, 'calendar_B.html', context)

def calendar_C(request):
    querydf=reservemodel2.objects.filter(category='C室')
    context = {
   'df_C' : querydf, 
 }
    return render(request, 'calendar_C.html', context)

def reserve(request):
    return render(request, 'reserve.html')

class Delete(DeleteView):
    model=reservemodel2
    template_name='delete.html'
    success_url=reverse_lazy('index')
    fields= ['checkin','time1','checkout','time2','category']
    
    
