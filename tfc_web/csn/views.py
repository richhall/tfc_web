from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from csn.models import LWDeviceForm, LWDevice, LWCallbackURLFormSet, LWApplication, LWApplicationForm


@login_required
def devices(request):
    return render(request, 'csn/devices.html', {
        'devices': LWDevice.objects.filter(user=request.user)
    })


@login_required
def new_device(request):
    lwdevice_form = LWDeviceForm(user=request.user)
    if request.method == "POST":
        lwdevice_form = LWDeviceForm(request.POST, user=request.user)
        if lwdevice_form.is_valid():
            lwdevice_form.save()
            return redirect('csn_home')
    return render(request, 'csn/new_device.html', {
        'form': lwdevice_form
    })


@login_required
def delete_device(request):
    if request.method == "POST":
        lwdevice = get_object_or_404(LWDevice, user=request.user, dev_eui=request.POST['dev_eui'])
        lwdevice.delete()
    return redirect('csn_home')


@login_required
def applications(request):
    return render(request, 'csn/applications.html', {
        'applications': LWApplication.objects.filter(user=request.user)
    })


@login_required
def new_application(request):
    lwapplication_form = LWApplicationForm()
    lwcallbackurls_form = LWCallbackURLFormSet()
    if request.method == "POST":
        lwapplication_form = LWApplicationForm(request.POST)
        lwcallbackurls_form = LWCallbackURLFormSet(request.POST)
        if lwapplication_form.is_valid():
            lwapplication = lwapplication_form.save(commit=False)
            lwcallbackurls_form = LWCallbackURLFormSet(request.POST, instance=lwapplication)
            if lwcallbackurls_form.is_valid():
                lwapplication.user = request.user
                lwapplication.save()
                lwcallbackurls_form.save()
                return redirect('csn_home')
    return render(request, 'csn/new_application.html', {
        'form': lwapplication_form,
        'inline_form': lwcallbackurls_form,
    })
