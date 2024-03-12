"""
Thông tin nhóm 
Lê Quang Tín, 22001643, K67KHMT&TT
Trần Giao Quỳnh, 22001635, K67KHMT&TT
Trần Viết , 22001639, K67KHMT&TT

Danh sách bài tập 

-Bài 4 (Tìm danh sách số nguyên dương của n) divisor()

"""

n = int(input("Nhập n: "))


# Cách 1
def divisor1(n):
    list = []
    for i in range(1, n + 1):
        if n % i == 0:
            list.append(i)
    print("Danh sách ước của", n, list)


# Cách 2
def divisor2(n):
    list2 = []
    print("Danh sách ước của", n, ":", end=" ")
    [list2.append(j) for j in range(1, int(n / 2 + 1)) if (n % j == 0)]
    list2.append(n)
    print(list2, end=" ")


divisor1(n)
divisor2(n)
