email = dict()

# Enter your receiver's name and his mail id in the dict

email['myself'] = 'myself@gmail.com'
email['father'] = 'father@gmail.com'
email['mother'] = 'mother@gmail.com'
email['friend'] = 'friend@gmail.com'


def mail(x):
    """Returns the receivers name and his email id if present in list"""
    for k, v in email.items():
        if x == k:
            return k, v


def check_email(x):
    """Checks whether the requested user is there in the list or not"""
    for m, n in email.items():
        if m == x:
            return 'True'
    return 'False'


if __name__ == '__main__':
    a, c = mail(input())
    print(a, c)
    b = check_email(input())
    print(b)
