from api.models import User

class Authenticate:
    """Authenticate user.
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self):
        """Authenticate user.
        """
        try:
            user = User.objects.get(username=self.username)
            if user.password == self.password:
                return user
            else:
                return None
        except User.DoesNotExist:
            return None