from django.shortcuts import render
from .forms import OrgdetailForm,EmpdetailForm
from .models import Orgdetail,Empdetail
from django.db import IntegrityError
from django.contrib import messages

# Create your views here. 

def org_page(request):
    if request.method=='POST':
        data=OrgdetailForm(request.POST)
        print(type(request.POST.get('name')))
        if data.is_valid():
            name=data.cleaned_data['name']
            rec=Orgdetail(name=name)
            try:
                rec.save()
            except IntegrityError:
                messages.warning(request, 'Name already exists.')
    fm=OrgdetailForm()
    data=Orgdetail.objects.all()
    return render(request,'course/org.html',{'data':data,'form':fm})


def emp_page(request):
    if request.method=='POST':
        data=EmpdetailForm(request.POST)
        if data.is_valid():
            name=data.cleaned_data['name']
            orgdetail=data.cleaned_data['orgdetail']
            rec=Empdetail(name=name,orgdetail=orgdetail)
            rec.save()
    fm=EmpdetailForm()
    data=Empdetail.objects.all()
    return render(request,'course/emp.html',{'data':data,'form':fm})