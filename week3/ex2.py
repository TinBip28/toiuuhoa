# Nhập vào tọa độ hai điểm A(x1;y1) và B(x2;y2) tìm ra phương trình đường thẳng đi qua hai điểm (d): ax + by = c


# Kiểm tra hai điểm có trùng nhau không
# def checkPoint(point1, point2):
#     return point1 == point2


def Enter_coordinates():
    print("Nhập tọa độ điểm A")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    point1 = (x1, y1)

    print("Nhập tọa độ điểm B")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    point2 = (x2, y2)
    return point1, point2


# Tìm tọa độ 3 điểm theo định nghĩa
def Linear_equations(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    # Tọa độ tích vô hướng
    a = y1 - y2
    b = x2 - x1

    c = (y1 - y2) * x1 + y1 * (x1 - x2)
    return a, b, c


# Biến đổi thành số nguyên nếu hợp lệ
def Zero_clear(coordinate):
    x = coordinate[0]
    y = coordinate[1]
    if x == int(x):
        x = int(x)
    if y == int(y):
        y = int(y)
    res = (x, y)
    print(res)
    return res


# Tìm ra phương trình đường thẳng
def Print_equation():
    points = Enter_coordinates()
    while points[0] == points[1]:
        print("Hai điểm trùng nhau!")
        points = Enter_coordinates()
    else:
        point_A = Zero_clear(points[0])
        point_B = Zero_clear(points[1])
        result = Linear_equations(point_A, point_B)
        print(
            "Phương trình mặt phẳng là: {}x + {}y = {}".format(
                result[0], result[1], result[2]
            )
        )
        print("a = {}, b = {}, c = {}".format(result[0], result[1], result[2]))


Print_equation()
