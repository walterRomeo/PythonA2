import random
from random import randint


def password_generator_min10(max_length: 'int', allowed_chars: 'str', seed=None) -> 'str':
    if max_length < 10:
        raise Exception("Password cannot be shorter then 10")
    if seed:
        random.seed(seed)
    length = int(randint(int(max_length - (max_length * 0.1)), max_length))
    new_generated_password = ''
    for i in range(length):
        new_generated_password += allowed_chars[randint(0, len(allowed_chars) - 1)]
    return new_generated_password
