mport os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wayuu_artesania.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Crear superusuario solo si no existe
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@raicesvivas.com',
        password='admin123'
    )
    print("Superusuario creado exitosamente")
else:
    print("El superusuario ya existe")
