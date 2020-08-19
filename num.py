number = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
          'nine': '9', 'ten': '10', 'eleven': '11', 'twelve': '12', 'thirteen': '13', 'fourteen': '14', 'fifteen': '15',
          'sixteen': '16', 'seventeen': '17', 'eighteen': '18', 'nineteen': '19', 'twenty': '20'}


def check(num):
    """Checks for a word whether it is a number or not"""
    for k, v in number.items():
        if k == num:
            return v
    return 'empty'


if __name__ == '__main__':
    print(number)
    a = check(input())
    print(a)
