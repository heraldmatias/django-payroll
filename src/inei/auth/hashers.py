import hashlib
import base64
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.utils.crypto import (pbkdf2, constant_time_compare, get_random_string)

class MyPBKDF2PasswordHasher(PBKDF2PasswordHasher):
    """ A subclass of PBKDF2PasswordHasher that uses 100 times more iterations. """
    iterations = 100
    digest = hashlib.sha512
    algorithm = "pbkdf2_sha512"

    def encode(self, password, salt, iterations=None):
        assert password is not None
        assert salt and '$' not in salt
        if not iterations:
            iterations = self.iterations
        hash = pbkdf2(password, '', iterations, digest=self.digest, dklen=40)
        hash = base64.b64encode(hash)
        return "%s" % hash

    def verify(self, password, encoded):
        encoded_2 = self.encode(password, '', int(self.iterations))
        return constant_time_compare(encoded, encoded_2)