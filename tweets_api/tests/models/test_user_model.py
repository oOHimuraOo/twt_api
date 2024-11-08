from django.test import TestCase
from tweets_api.models import User


class UsuarioModelTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create(
            nome="TestUser",
            senha="TestPassword"
        )

    def test_usuario_creation(self):
        self.assertEqual(self.usuario.nome, "TestUser")
        self.assertTrue(isinstance(self.usuario, User))
        self.assertEqual(str(self.usuario), "TestUser")

    def test_usuario_profile_default(self):
        self.assertEqual(self.usuario.profile, "images/profile_default.svg")
