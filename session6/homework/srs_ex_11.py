def is_inside(point, rectangle):
    criterion_1 = rectangle[0] <= point[0] <= (rectangle[0] + rectangle[2])
    criterion_2 = rectangle[1] <= point[1] <= (rectangle[1] + rectangle[3])
    if criterion_1 and criterion_2:
        return True
    else:
        return False
