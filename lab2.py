from pprint import pprint
my_dict = {'first': 'so easy'}

def dict_maker(**kwargs):
    my_dict.update(**kwargs)

dict_maker(a1 = 335551, a2 = 343510, a3 = 1255, a4 = 525)
dict_maker(name = 'Егор', age = 21, weight = 160, eyes_color = 'blue')
pprint(my_dict)