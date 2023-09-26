def Calculate_Area(length, width):

    if length == width:
        return "This is a square!"

    return length * width


length = float(input("enter length:"))
width = float(input("enter width:"))

area = Calculate_Area(length, width)
print(area)  #
