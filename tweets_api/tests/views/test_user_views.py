from rest_framework.test import APITestCase
from rest_framework import status
from tweets_api.models import User


class UsuarioAPITest(APITestCase):
    def test_create_usuario(self):
        data = {
            "nome": "NewUser",
            "senha": "NewPassword"
        }
        response = self.client.post('/api/usuarios/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().nome, "NewUser")

    def test_get_usuario_list(self):
        User.objects.create(nome="User1", senha="Pass1")
        response = self.client.get('/api/usuarios/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
