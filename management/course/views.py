from django.shortcuts import render
from .forms import OrgdetailForm,EmpdetailForm
from .models import Orgdetail,Empdetail

# Create your views here. 

def org_page(request):
    if request.method=='GET':
        fm=OrgdetailForm()
    elif request.method=='POST':
        data=OrgdetailForm(request.POST)
        if data.is_valid():
            name=data.cleaned_data['name']
            rec=Orgdetail(name=name)
            rec.save()
        fm=OrgdetailForm()
    return render(request,'course/org.html',{'form':fm})


def emp_page(request):
    if request.method=='GET':
        emp=EmpdetailForm()
    elif request.method=='POST':
        data=EmpdetailForm(request.POST)
        if data.is_valid():
            name=data.cleaned_data['name']
            orgdetail=data.cleaned_data['orgdetail']
            rec=Empdetail(name=name,orgdetail=orgdetail)
            rec.save()
        emp=EmpdetailForm()
    return render(request,'course/emp.html',{'form':emp})