from DataStructures.List  import array_list as al

def new_list():
    newlist = {
        'elements':[],
        'size': 0,
    }
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):

    size = my_list["size"]
    if size > 0:
        keyexist = false
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first (my_list,e):
    my_list = al.new_list()
    my_list = al.add_first(my_list,1)

    return my_list


def add_last (my_list,e):
    my_list = al.new_list()
    my_list = al.add_last(my_list,1)

    return my_list

def size (my_list):
    my_list = al.new_list()
    print(al.size(my_list))

def first_element (my_list):
    my_list = al.new_list()
    print(al.first_element(my_list))