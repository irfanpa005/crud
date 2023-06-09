from django.shortcuts import render
from django.urls import reverse
from .models import crud
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def index(request):
    data = crud.objects.all()
    return render(request,'index.html',{"datas":data})

def save_data(request):
        if request.method == 'POST':
            sl_no = request.POST.get('slno')
            item_name = request.POST.get('itemname')
            description = request.POST.get('description')
            cr = crud(sl_no=sl_no,item_name=item_name,description=description)
            cr.save()
            messages.info(request, "Data Created Successfully")
        return HttpResponseRedirect(reverse('index'))


def update(request,data_id):
    data = crud.objects.get(pk=data_id)
    data_all = crud.objects.all()
    if request.method == 'POST':
            sl_no = request.POST.get('slno')
            item_name = request.POST.get('itemname')
            description = request.POST.get('description')
            crud.objects.filter(id=data_id).update(sl_no=sl_no,item_name=item_name,description=description)
            messages.info(request, "Data Updated Successfully")
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'update.html',{"datas":data,"data_all":data_all})


def delete(request,data_id):
    if request.method == 'POST':
        cr = crud.objects.get(id=data_id)
        cr.delete()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'delete.html', {'crud': crud})
