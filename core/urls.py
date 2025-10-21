from django.urls import path
from .views import (
    index,
    owners_list,
    owner_create,
    pets_list,
    pet_create,
    appointments_list,
    appointment_create,
)

urlpatterns = [
    path("", index, name="home"),
    path("propietarios/", owners_list, name="owners_list"),
    path("propietarios/crear/", owner_create, name="owner_create"),
    path("mascotas/", pets_list, name="pets_list"),
    path("mascotas/crear/", pet_create, name="pet_create"),
    path("citas/", appointments_list, name="appointments_list"),
    path("citas/crear/", appointment_create, name="appointment_create"),
]
