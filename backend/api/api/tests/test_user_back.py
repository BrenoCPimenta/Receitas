from django.test import TestCase
from api.models import User

class UserTestCase(TestCase):

    def test_creating_and_recovering_user(self):
        user = User(
            username='new_user',
            password='password',
            name='new_user',
            email='new_user@new_user.com')
        user.save()

        user_recovered = User.objects.get(username='new_user')
        self.assertEqual(user_recovered, user_recovered)
