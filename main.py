import random
import string
from collections import Counter
from math import log


def password_generator():
    len_password = random.randint(8, 16)
    password = ''.join(random.choice(string.ascii_letters +
                       string.digits + string.punctuation) for i in range(len_password))
    return password


def shannon(password):
    counts = Counter(password)
    frequencies = ((i / len(password)) for i in counts.values())
    return - sum(f * log(f, 2) for f in frequencies)


def s(i): return - sum(f * log(f, 2)
                       for f in ((j / len(i)) for j in Counter(i).values()))


def level(password, entropy=shannon):
    entropy = entropy(password)
    if entropy < 1.5:
        return 'Very weak'
    elif entropy < 2:
        return 'Weak'
    elif entropy < 2.5:
        return 'Medium'
    elif entropy < 3:
        return 'Strong'
    else:
        return 'Very strong'


if __name__ == '__main__':
    password = password_generator()
    print('Password: ',
          password,
          '\nEntropy: ',
          s(password),
          '\nLevel: ',
          level(password))
