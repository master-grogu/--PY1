def get_random_password(n=8) -> str:
    import random
    import string
    return random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=n)


print(get_random_password())
