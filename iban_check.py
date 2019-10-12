import string
import iban_const

LETTERS = {ord(d): str(i) for i, d in enumerate(string.digits + string.ascii_uppercase)}


def _number_iban_2(iban):
    return ''.join([LETTERS[ord(l)] for i, l in enumerate((iban[4:] + iban[:4]).upper())])


# def _number_iban(iban):
#     return (iban[4:] + iban[:4]).translate(LETTERS)
#

def generate_iban_check_digits(iban):
    number_iban = _number_iban_2(iban[:2] + '00' + iban[4:])
    return '{:0>2}'.format(98 - (int(number_iban) % 97))


def valid_iban(iban):
    return int(_number_iban_2(iban)) % 97 == 1


def is_ok(iban):
    try:
        check = iban_const.IBAN_COUNTRIES[iban[0:2]]
        # print(check)
        return len(iban) <= check[0] and (not check[1] or generate_iban_check_digits(iban) == iban[2:4]) and valid_iban(iban)
    except KeyError:
        return False


if __name__ == '__main__':
    my_iban = 'RO13RZBR0000060007134800'
    # print(_number_iban(my_iban))
    print(_number_iban_2(my_iban))
    print(is_ok(my_iban))

    if generate_iban_check_digits(my_iban) == my_iban[2:4] and valid_iban(my_iban):
        print('IBAN ok!\n')
    else:
        print('IBAN not ok!\n')