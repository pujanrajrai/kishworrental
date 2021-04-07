from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForms
from .models import Profile


def create(request):
    if Profile.objects.filter(owner=request.user).exists():
        return redirect('profiles:view')
    if request.method == 'POST':
        forms = ProfileForms(request.POST, request.FILES)
        if forms.is_valid():
            seller_profile = Profile(
                owner=request.user,
                profile_image=request.FILES['profile_image'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                mobile_number=request.POST['mobile_number'],
                citizenship_number=request.POST['citizenship_number'],
                temp_address=request.POST['temp_address'],
                per_address=request.POST['per_address'],
                citizenship_front=request.FILES['citizenship_front'],
                citizenship_back=request.FILES['citizenship_back'],
            )
            seller_profile.save()
            return redirect('profiles:view')
        else:
            print(forms.errors)
    return render(request, 'profiles/create.html')


def view(request):
    return render(request, 'profiles/view.html')
