def is_inside(point, rectangle):
    criterion_1 = rectangle[0] <= point[0] <= (rectangle[0] + rectangle[2])
    criterion_2 = rectangle[1] <= point[1] <= (rectangle[1] + rectangle[3])
    if criterion_1 and criterion_2:
        return True
    else:
        return False

inside_case = is_inside([200, 120], [140, 60, 100, 200])
outside_case = is_inside([100, 120], [140, 60, 100, 200])

if inside_case == True and outside_case == False:
    print("Your function is correct")
else:
    print("You failed")
