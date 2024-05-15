"""
Thông tin nhóm
Lê Quang Tín, 22001643, K67KHMT&TT
Trần Giao Quỳnh, 22001635, K67KHMT&TT
Trần Viết Thành, 22001638, K67KHMT&TT

Danh sách bài tập
- Bài 2a. oxy_equation()
- Bài 4. n_queens_solver()
"""

# Bài 2a


# Nhập tọa độ hai điểm
def enter_coordinates():
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
def linear_equations(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    # Tọa độ tích vô hướng
    a = y1 - y2
    b = x2 - x1

    c = (y1 - y2) * x1 + y1 * (x1 - x2)
    # Trả về một tuple chứa hệ số của phương trình đường thẳng
    return a, b, c


# Biến đổi thành số nguyên nếu hợp lệ
def zero_clear(coordinate):
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
def oxy_equation():
    points = enter_coordinates()
    while points[0] == points[1]:
        print("Hai điểm trùng nhau!")
        points = enter_coordinates()
    else:
        point_A = zero_clear(points[0])
        point_B = zero_clear(points[1])
        result = linear_equations(point_A, point_B)
        print(
            "Phương trình mặt phẳng là: {}x + {}y = {}".format(
                result[0], result[1], result[2]
            )
        )
        print("a = {}, b = {}, c = {}".format(result[0], result[1], result[2]))


oxy_equation()
print("============================================================================")


# Bài 2b


def phuong_trinh_mat_phang(point1, point2, point3):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    x3, y3, z3 = point3
    # Vecto 12
    x12 = x2 - x1
    y12 = y2 - y1
    z12 = z2 - z1
    # Vecto13
    x13 = x3 - x1
    y13 = y3 - y1
    z13 = z3 - z1
    # Tich co huong cua 13 va 12
    a = y12 * z13 - z12 * y13
    b = z12 * x13 - z13 * x12
    c = x12 * y13 - x13 * y12
    d = a * x1 + b * y1 + c * z1
    return a, b, c, d


# check trung nhau
def check_trung(point1, poin2, point3):
    return point1 == point2 | point2 == point3 | point3 == point1


# check xem 3 diem co trung mat phang khong
def check_cung_mat_phang(tmp):
    return tmp[0] == 0 & tmp[1] == 0 & tmp[2] == 0 & tmp[3] == 0


# nhap cac diem
def oxyz_equation():
    try:
        print("nhap vao toa do diem dau tien:")
        x1 = int(input("nhap vao x1: "))
        y1 = int(input("nhap vao y1: "))
        z1 = int(input("nhap vao z1: "))

        print("nhap vao toa do diem thu hai:")
        x2 = int(input("nhap vao x2: "))
        y2 = int(input("nhap vao y2: "))
        z2 = int(input("nhap vao z2: "))

        print("nhap vao toa do diem thu ba: ")
        x3 = int(input("nhap vao x3: "))
        y3 = int(input("nhap vao y3: "))
        z3 = int(input("nhap vao z3: "))

        point1 = (x1, y1, z1)
        point2 = (x2, y2, z2)
        point3 = (x3, y3, z3)

        result = phuong_trinh_mat_phang(point1, point2, point3)
        if check_trung == True:
            print("Cac diem trung nhau")
        elif check_cung_mat_phang(result) == True:
            print("Cac diem da nhap vao cung mat phang")
        else:
            print(
                "Phương trình mặt phẳng là: {}x + {}y + {}z = {}".format(
                    result[0], result[1], result[2], result[3]
                )
            )
            print(
                "a = {}, b = {}, c = {}, d = {}".format(
                    result[0], result[1], result[2], result[3]
                )
            )
    except ValueError:
        print("Vui long nhap so nguyen")


oxyz_equation()

print("==========================================================================")

import gurobipy as gp
from gurobipy import GRB


# Kiểm tra liệu đầu vào hợp lệ hay không
def n_check(n):
    if not type(n) is int:
        return False
    if n <= 0 or (n > 1 and n < 4):
        return False
    return True


# Mô hình tối ưu
def n_queens(n):
    model = gp.Model("N_Queens")

    chess = {}
    # Khơi tạo ma trận
    for x in range(n):
        for y in range(n):
            chess[x, y] = model.addVar(
                lb=0, ub=1, vtype=GRB.BINARY, name=f"pos[{x}_{y}]"
            )

    # Hàm mục tiêu
    model.setObjective(
        gp.quicksum(chess[i, j] for i in range(n) for j in range(n)), GRB.MAXIMIZE
    )
    # Hàm điều kiện
    for i in range(n):
        # Tổng cột, hàng == 1
        model.addConstr(gp.quicksum(chess[i, y] for y in range(n)) == 1)
        model.addConstr(gp.quicksum(chess[x, i] for x in range(n)) == 1)

    # Điều kiện cho hàng đường chéo từ trái qua phải
    for k in range(-n + 1, n):
        diagonal = [(x, y) for x in range(n) for y in range(n) if x - y == k]
        model.addConstr(gp.quicksum(chess[x, y] for x, y in diagonal) <= 1)

    # Điều kiện cho hàng đường chéo phải qua trái
    for k in range(0, n * 2 - 1):
        diagonal = [(x, y) for x in range(n) for y in range(n) if x + y == k]
        model.addConstr(gp.quicksum(chess[x, y] for x, y in diagonal) <= 1)

    # Biến đếm lời giải
    solutions = 0
    while True:
        model.optimize()
        match model.status:
            case GRB.OPTIMAL:
                solutions += 1
                result = []
                for i in range(n):
                    for j in range(n):
                        if chess[i, j].x == 1:
                            result.append((i, j))
                    model.addConstr(
                        gp.quicksum(chess[i, j] for i, j in result) <= n - 1
                    )
            case GRB.INFEASIBLE:
                break
            case _:
                raise ValueError(f"Error")
    print(f"\n Số lượng lời giải: {solutions}")


def n_queens_solver():
    n = int(input("Nhập số lượng quân hậu: "))
    while n_check(n) == False:
        n = int(input("Nhập lại: "))
    n_queens(n)
