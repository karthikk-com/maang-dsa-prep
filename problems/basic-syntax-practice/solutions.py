def calculate_rect_area () :
    length = float(input("Enter the length of the rectangle : "))
    breadth = float(input("Enter the breadth of the rectangle : "))

    if (length >= 0 and breadth >=0) :
        area = length * breadth
        return area

    return "error"


print(calculate_rect_area())