def get_even_list(l):
    even_list = []
    for integer in l:
        if integer % 2 == 0:
            even_list.append(integer)
    return(even_list)

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
