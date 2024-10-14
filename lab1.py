request = int(input('Введите номер кабинета: '))

dictionary = {
    101: {'key': 1234, 'access': True},
    102: {'key': 1333, 'access': False},
    103: {'key': 2222, 'access': True},
    104: {'key': 3535, 'access': False},
    None: {'key': None, 'access': False}
}

response = dictionary.get(request)
if not response:
    response = dictionary[None]
key = response.get('key')
access = response.get('access')
print(key, access)