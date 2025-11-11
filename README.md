💡 Descripción del proyecto

Este es un proyecto desarrollado con Django como parte del curso de CoderHouse.
El objetivo fue crear una aplicación web que implemente el patrón MVT (Model–View–Template), incluyendo herencia de plantillas, formularios para ingreso de datos y búsquedas en base de datos.

El tema elegido fue una web estilo blog educativo, donde se pueden gestionar Cursos, Profesores, Estudiantes y Entregables.

🏗️ Estructura del proyecto
TuPrimeraEntregaHernandez/
│
├── blog/                        # App principal
│   ├── migrations/
│   ├── static/                  # Archivos estáticos (CSS, imágenes)
│   ├── templates/               # Plantillas HTML
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── blog/
│   │   │   ├── profesor_form.html
│   │   │   ├── curso_form.html
│   │   │   ├── estudiante_form.html
│   │   │   ├── entregable_form.html
│   ├── admin.py                 # Registro de modelos en el panel admin
│   ├── models.py                # Definición de clases (Modelos)
│   ├── views.py                 # Lógica de las vistas
│   ├── forms.py                 # Formularios personalizados
│   ├── urls.py                  # Rutas
│
├── db.sqlite3                   # Base de datos local
├── manage.py                    # Comando principal de Django
└── requirements.txt             # Dependencias del proyecto

⚙️ Instalación y configuración

Clonar el repositorio

git clone https://github.com/melhernandezvi-code/TuPrimeraPaginaHernandez.git
cd TuPrimeraPaginaHernandez


Crear entorno virtual

python3 -m venv .venv
source .venv/bin/activate  # En macOS/Linux
# .venv\Scripts\activate   # En Windows


Instalar dependencias

pip install -r requirements.txt


Realizar las migraciones

python3 manage.py makemigrations
python3 manage.py migrate


Crear superusuario

python3 manage.py createsuperuser


Ejemplo:

Username: meltest
Email: meltest@test.com
Password: 123qweasD


Ejecutar el servidor

python3 manage.py runserver


Luego visitar 👉 http://127.0.0.1:8000

🌐 Funcionalidades principales

✅ Home:
Página principal con fondo ilustrado, buscador de cursos y acceso al resto de secciones.

✅ Profesores:
Formulario con validación por campos (solo letras, todos obligatorios).
Mensaje de confirmación con animación de confeti al guardar.

✅ Cursos:
Formulario alineado con los mismos estilos de la sección profesores.
Campos: nombre y camada (número).

✅ Estudiantes:
Formulario estilizado con los mismos estilos, campos: nombre, apellido, email.

✅ Entregables:
Formulario con fecha y checkbox de entrega, con validaciones requeridas.

✅ Panel de administración (Django Admin):
Gestión completa de todos los modelos desde una interfaz administrativa.

🧱 Modelos
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.camada}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} - {'Entregado' if self.entregado else 'Pendiente'}"

🔍 Búsqueda en base de datos

En la página principal se incluye un campo para buscar cursos por número de camada.
Los resultados se muestran dinámicamente en el mismo template home.html.

👩‍💻 Autora

Melanie Hernández
📧 melhernandezvi@gmail.com

🌎 Proyecto del curso Python — CoderHouse