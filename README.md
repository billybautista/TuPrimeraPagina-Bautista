# TuPrimeraPagina-Bautista

Sistema de gestión "Fido"

## Instalación

```bash
# crear entorno virtual
python -m venv entorno
source entorno/bin/activate

# instalar dependencias
pip install -r requirements.txt

# migrar base de datos
python manage.py migrate

# correr servidor
python manage.py runserver
```

## Funcionalidades

- Gestión de dueños de mascotas
- Registro de mascotas (pendiente)
- Sistema de citas (pendiente)

# Pasos para probar

1. Crear un dueño ( Nombre, Email, Teléfono )
2. Crear una mascota ( Nombre , Edad, Tipo, Raza, Dueño)
3. Crear una cita ( Mascota, Fecha, Hora, Motivo)

## Notas

- Usando Django 5.2.7
- Base de datos SQLite
- Tailwind CSS para estilos
