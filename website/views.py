from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records=Record.objects.all()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'You Have Been logged In Successfully!!')
            return redirect('home')
        else:
            messages.success(request,'Oops!! something went wrong ,Please Try Again!!')
            return redirect('home')
    else:
        return render(request,'home.html',{'records':records})


def logout_user(request):
    logout(request)
    messages.success(request,'You have Been Successfully Logged Off!!')
    return redirect('home')

def register_user(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request, user)
            messages.success(request,'You have succesfully logged In!!')
            return redirect('home')
    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})


def customer_record(request,pk):
    if request.user.is_authenticated:
        cust_record=Record.objects.get(id=pk)
        return render(request,'record.html',{'cust_record':cust_record})
    else:
        messages.success(request, 'You must Be logged In to View That Page')
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
        record_del=Record.objects.get(id=pk)
        record_del.delete()
        messages.success(request, 'You have deleted the record Successfully!!')
        return redirect('home')
    else:
        messages.success(request, 'You must Be logged In to Delete That Record')
        return redirect('home')

def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=='POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'You have added the record Successfully!!')
                return redirect('home')
        return render(request, 'add_record.html',{'form':form})
    else:
        messages.success(request, 'You must Be logged In to add That Record')
        return redirect('home')

def update_record(request,pk):
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=pk)
        form=AddRecordForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have Updated the record Successfully!!')
            return redirect('home')
        return render(request, 'update_record.html',{'form':form})

    else:
        messages.success(request, 'You must Be logged In to add That Record')
        return redirect('home')