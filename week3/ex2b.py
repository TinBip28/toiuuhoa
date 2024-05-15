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
