from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OwnerForm, PetForm
from .models import Owner, Pet


def index(request):
    # Dashboard
    return render(request, "core/index.html")


def owners_list(request):
    # Lista de dueños
    query = request.GET.get("q", "")
    owners = Owner.objects.all().order_by("-created_at")

    # Buscar por nombre o email
    if query:
        owners = owners.filter(name__icontains=query) | owners.filter(
            email__icontains=query
        )

    return render(request, "core/owners.html", {"owners": owners, "query": query})


def owner_create(request):
    # Crear dueño
    if request.method == "POST":
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Dueño creado exitosamente!")
            return redirect("owners_list")
    else:
        form = OwnerForm()

    return render(request, "core/owner_create.html", {"form": form})


def pets_list(request):
    # Lista de mascotas
    query = request.GET.get("q", "")
    pets = Pet.objects.all().order_by("-created_at")

    # Buscar por nombre
    if query:
        pets = pets.filter(name__icontains=query)

    return render(request, "core/pets.html", {"pets": pets, "query": query})


def pet_create(request):
    # Crear mascota
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Mascota creada exitosamente!")
            return redirect("pets_list")
    else:
        form = PetForm()
    return render(request, "core/pet_create.html", {"form": form})


def appointments_list(request):
    # Lista de citas
    return render(request, "core/appointments.html")
