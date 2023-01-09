import random, string

def get_random_name(length):
    all_letters = string.ascii_letters+string.digits
    all_letters = list(all_letters)
    all_letters = random.sample(all_letters,len(all_letters))
    name= all_letters[:length]
    return "".join(name)
