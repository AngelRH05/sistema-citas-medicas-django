# Sistema de citas médicas

Aplicación web académica desarrollada con **Python, Django y SQLite** para gestionar citas médicas. Proyecto de Angel Gabriel Reyes Huayta, estudiante de Ingeniería de Sistemas en la Universidad San Ignacio de Loyola.

## Funcionalidades

- Listado de citas ordenadas por fecha.
- Registro, edición y eliminación de citas con confirmación.
- Asociación de cada cita con un doctor y un paciente.
- Estados: programada, atendida y cancelada.
- Validación de fechas: deben ser posteriores al día actual.
- Administración de doctores y citas desde Django Admin.
- Datos ficticios de demostración y pruebas automatizadas.

## Tecnologías

| Componente | Tecnología |
| --- | --- |
| Lenguaje | Python 3.12 o superior |
| Framework | Django 6.0.4 |
| Base de datos | SQLite |
| Interfaz | Plantillas de Django, HTML y CSS |

## Ejecutar en Windows (PowerShell)

```powershell
git clone https://github.com/AngelRH05/sistema-citas-medicas-django.git
cd sistema-citas-medicas-django
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py seed_demo
.\.venv\Scripts\python.exe manage.py runserver
```

Abrir **http://127.0.0.1:8000/**. El comando `seed_demo` crea un doctor y un paciente ficticios; no incluye información de personas reales.

Para administrar doctores desde **http://127.0.0.1:8000/admin/**:

```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
```

En Linux/macOS, crear el entorno con `python3 -m venv .venv` y sustituir `.\.venv\Scripts\python.exe` por `.venv/bin/python`.

## Comprobaciones

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test
```

Las pruebas cubren el flujo de creación, edición y eliminación, fechas inválidas, estados inválidos, registros inexistentes y el listado vacío.

## Estructura

```text
clinica/           Configuración y rutas del proyecto
citas/             Modelos, formularios, vistas y rutas de citas
  migrations/      Esquema de la base de datos
  templates/       Interfaz web
  management/      Comando de datos de demostración
manage.py          Herramientas de administración de Django
requirements.txt   Dependencias
```

## Alcance y próximos pasos

Es un prototipo académico para ejecución local. Las vistas de citas todavía no requieren inicio de sesión y no se comprueban conflictos de horario. La fecha de una cita existente también debe ser futura para poder editarla. Como siguientes mejoras se plantean autenticación, permisos, horarios y filtros.

La clave original de desarrollo y la base de datos local se excluyeron de esta publicación. La aplicación genera una clave temporal si no se define `DJANGO_SECRET_KEY`; esto puede invalidar sesiones al reiniciar. Para conservarlas, definir una clave propia mediante esa variable de entorno. La configuración de depuración está habilitada por defecto para uso local; `DJANGO_DEBUG=0` la desactiva y `DJANGO_ALLOWED_HOSTS` permite indicar hosts separados por comas. El proyecto requiere configuración adicional antes de cualquier despliegue.

## Sobre esta versión

Parte del proyecto académico PC01. Se organizó para su publicación, se corrigieron las plantillas y los enlaces de acciones, y se añadieron documentación, datos ficticios y pruebas.
