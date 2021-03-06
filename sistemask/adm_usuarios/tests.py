from django.test import TestCase

from adm_usuarios.models import Usuario

# Create your tests here.

class UserTest(TestCase):

    def setUp(self):
        print(':::::::::::Inicia pruebas unitarias de ABM USUARIO:::::::::::')
        u1 = Usuario.objects.create(username= 'isidro',nombre = 'Isidro', apellido = 'Brizuela', password = 'isidro', cedula = 3841270)
        u2 = Usuario.objects.create(username= 'juan',nombre = 'Juan', apellido = 'Benitez', password = 'juan', cedula = 3841270, email='isaubripi@gmail.com', estado = True)
        print('Creacion de Usuarios ejecutada exitosamente')

    def test_user(self):
        u1 = Usuario.objects.get(username = 'isidro')
        self.assertEqual(u1.username, 'isidro')
        print('Comparacion de atributos')

    def test_name(self):
        u1 = Usuario.objects.get(nombre= 'Isidro')
        self.assertEqual(u1.nombre, 'Isidro')
        print('Comparacion de atributos2')


