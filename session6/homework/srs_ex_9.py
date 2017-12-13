def get_even_list(l):
    even_list = []
    for integer in l:
        if integer % 2 == 0:
            even_list.append(integer)
    return even_list
