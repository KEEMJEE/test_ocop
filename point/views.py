from django.shortcuts import render, redirect, get_object_or_404
from .models import Carbonpoint, Greenpoint, Carbon
from .forms import CarbonForm, GreenForm
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def Createcarbon(request):
    """
    admin계정만 들어와서 포인트 종류 입력 가능
    """
    if request.method == 'POST':
        form = CarbonForm(request.POST)
        if form.is_valid():
            carbonpoint = form.save(commit=False)
            carbonpoint.create_date = timezone.now()
            carbonpoint.save()
            return redirect('point:carbonlist')
    else:
        form = CarbonForm()

    context = {'form': form}
    return render(request, 'point/carbonform.html', context)

def Creategreen(request):
    """
    admin계정만 들어와서 포인트 종류 입력 가능
    """
    if request.method == 'POST':
        form = GreenForm(request.POST)
        if form.is_valid():
            greenpoint = form.save(commit=False)
            greenpoint.create_date = timezone.now()
            greenpoint.save()
            return redirect('point:greenlist')
    else:
        form = GreenForm()

    context = {'form': form}
    return render(request, 'point/greenform.html', context)

def Carbonlist(request):
    """
    탄소포인트, 그린포인트 목록을 보여주고 수정 추가 삭제 가능
    """
    carbonlist = Carbonpoint.objects.order_by('create_date')
    context = {'carbonlist': carbonlist}
    return render(request, 'point/carbonlist.html', context)

def Greenlist(request):
    """
    탄소포인트, 그린포인트 목록을 보여주고 수정 추가 삭제 가능
    """
    greenlist = Greenpoint.objects.order_by('create_date')
    context = {'greenlist': greenlist}
    return render(request, 'point/greenlist.html', context)

def Carbon_Modify(request, Carbonpoint_id):
    """
    admin계정만 들어와서 포인트 수정 가능
    """
    carbon = get_object_or_404(Carbonpoint, pk=Carbonpoint_id)

    if request.method == 'POST':
        form = CarbonForm(request.POST, instance = carbon)
        if form.is_valid():
            carbonpoint = form.save(commit=False)
            carbonpoint.modify_date = timezone.now()
            carbonpoint.save()
            return redirect('point:carbonlist')
    else:
        form = CarbonForm(instance=carbon)

    context = {'form': form}
    return render(request, 'point/carbonmodify.html', context)

def Green_Modify(request, Greenpoint_id):
    """
    admin계정만 들어와서 포인트 수정 가능
    """
    green = get_object_or_404(Greenpoint, pk=Greenpoint_id)

    if request.method == 'POST':
        form = GreenForm(request.POST, instance = green)
        if form.is_valid():
            greenpoint = form.save(commit=False)
            greenpoint.modify_date = timezone.now()
            greenpoint.save()
            return redirect('point:greenlist')
    else:
        form = GreenForm(instance=green)

    context = {'form': form}
    return render(request, 'point/greenmodify.html', context)

def Carbon_Delete(request, Carbonpoint_id):
    """
    탄소포인트 삭제
    """
    carbon = get_object_or_404(Carbonpoint, pk = Carbonpoint_id)

    carbon.delete()
    return redirect('point:carbonlist')

def Green_Delete(request, Greenpoint_id):
    """
    그린포인트 삭제
    """
    green = get_object_or_404(Greenpoint, pk = Greenpoint_id)

    green.delete()
    return redirect('point:greenlist')




def Carbonpage(request):
    """
    탄소페이지 보여줌
    """
    carbon_list = Carbonpoint.objects.order_by('create_date')
    context = {'carbon_list': carbon_list}
    return render(request, 'point/carbon.html', context)

def Greenpage(request):
    """
    그린페이지 보여줌
    """
    green_list = Greenpoint.objects.order_by('create_date')
    context = {'green_list': green_list}
    return render(request, 'point/green.html', context)




#
# def add_carbon(request):
#     selpoint = Carbonpoint.objects.get(id=Carbonpoint.id)
#
#     try:
#
# def my_carbon():
