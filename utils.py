import random
import string


def generate_id():
    return ''.join(random.sample(string.ascii_letters + string.digits, 10))
