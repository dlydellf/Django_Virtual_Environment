from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ProfileForm
from .models import Profile


def profile_list(request):
    profiles = Profile.objects.all() # 'profiles' references nothing; it's an arbitrary variable
    return render(request, 'profiles/profiles_page.html', {'profiles': profiles}) # the  'profiles' value references 'profiles'


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Profile, pk=pk) # "Profile' frm models.py / red 'pk' == dictionary object, blue 'pk' == line 13
    form = ProfileForm(data=request.POST or None, instance=item) # 'instance' == backfill form with details from 'item'
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('profile_list')
        else:
            print(form.errors)
    else:
        return render(request, 'profiles/profiles_details.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('profile_list')
    context = {"item": item}
    return render(request, "profiles/confirmDelete.html", context)


def confirmed(request):
    if request.method == 'POST':
        # creates form instance & binds data to it:
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('profile_list')
    else:
        return redirect('profile_list')


def addProfile(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile_list')
    else:
        print(form.errors)
        form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'profiles/addProfile.html', context)
