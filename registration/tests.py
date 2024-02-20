from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Prueba unitaria que nos permite comprobar que despues de crear un usuario se ha creado automaticamente un perfil enlazado a el.

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test', 'test@test.com', 'test1234')
    
    def test_profile_exist(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)
        
        
    
    
