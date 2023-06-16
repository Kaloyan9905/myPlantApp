from django.shortcuts import render, redirect

from myPlantApp.web.forms import ProfileCreateForm, PlantCreateForm, PlantDeleteForm, PlantEditForm, \
    ProfileEditForm, ProfileDeleteForm
from myPlantApp.web.models import Profile, Plant


def index(request):
    profile = Profile.objects.all()

    context = {
        'profile': profile,
    }

    return render(request, 'home-page.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def details_profile(request):
    profile = Profile.objects.get()
    total_start = Plant.objects.count()

    context = {
        'profile': profile,
        'total_stars': total_start,
    }

    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.get()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()

            return redirect('details profile')

    context = {
        'form': form,
        'profile': Profile.objects.get(),
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.get()
    plants = Plant.objects.all()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)

        if form.is_valid():
            profile.delete()
            plants.delete()

            return redirect('index')

    context = {
        'form': form,
        'profile': Profile.objects.get(),
    }

    return render(request, 'delete-profile.html', context)


def catalogue(request):
    plants = Plant.objects.all()

    context = {
        'plants': plants,
        'profile': Profile.objects.get(),
    }

    return render(request, 'catalogue.html', context)


def create_plant(request):
    if request.method == 'GET':
        form = PlantCreateForm()
    else:
        form = PlantCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('catalogue')

    context = {
        'form': form,
        'profile': Profile.objects.get(),
    }

    return render(request, 'create-plant.html', context)


def details_plant(request, plant_id):
    plant = Plant.objects \
        .filter(pk=plant_id) \
        .get()

    context = {
        'plant': plant,
        'profile': Profile.objects.get(),
    }

    return render(request, 'plant-details.html', context)


def edit_plant(request, plant_id):
    plant = Plant.objects \
        .filter(pk=plant_id) \
        .get()

    if request.method == 'GET':
        form = PlantEditForm(instance=plant)
    else:
        form = PlantEditForm(request.POST, instance=plant)

        if form.is_valid():
            form.save()

            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
        'profile': Profile.objects.get(),
    }

    return render(request, 'edit-plant.html', context)


def delete_plant(request, plant_id):
    plant = Plant.objects \
        .filter(pk=plant_id) \
        .get()

    if request.method == 'GET':
        form = PlantDeleteForm(instance=plant)
    else:
        form = PlantDeleteForm(request.POST, instance=plant)

        if form.is_valid():
            plant.delete()

            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
        'profile': Profile.objects.get(),
    }

    return render(request, 'delete-plant.html', context)
