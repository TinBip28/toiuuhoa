import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt
import numdifftools as nd

"""
Thông tin nhóm
Lê Quang Tín - 22001643
Trần Giao Quỳnh - 22001638
Trần Viết Thành - 22001635

Danh sách bài tập
Bài 2: Gradient Descent : Hàm f(x, y) = 5x^2 + 2y
def func(x, y), gradient_func(x, y), GD_fixed_step_size(...), GD_backtracking_linesearch(...), draw_plot(...)
Bài 3: Newton's Method :

"""


def func(x, y):
    return 5 * x**2 + y * 2


def gradient_func(x, y):
    return np.array([10 * x, 2 * y])


init_point = np.array([-1, -1])
print(init_point[0], init_point[1])
eps = 1e-6
max_iteration = 400
aplha = 0.05


def GD_fixed_step_size(f, grad_f, init, alpha, eps, max_iteration):
    # alpha:độ dài bước cố định
    point = []
    x = init
    x_t = init - alpha * grad_f(x[0], x[1])
    for i in range(max_iteration):
        if norm(x - x_t) < eps:
            break
        x = x_t
        x_t = x - alpha * grad_f(x[0], x[1])
        point.append([x[0], x[1], f(x[0], x[1])])
    return x, point


def GD_backtracking_linesearch(f, grad_f, init, eps, max_iteration):
    point = []
    alpha = 0.01
    beta = 0.8
    x = init
    x_t = x - alpha * grad_f(x[0], x[1])
    for i in range(max_iteration):
        if norm(x - x_t) < eps:
            break
        t = 1
        x_t = x - t * alpha * grad_f(x[0], x[1])
        norm_2 = norm(grad_f(x[0], x[1])) ** 2
        f_x = f(x[0], x[1])
        X = x - t * grad_f(x[0], x[1])
        while f(X[0], X[1]) > f_x - 1 / 2 * t * alpha * norm_2:
            t *= beta
            X = x - t * alpha * grad_f(x[0], x[1])
        x = X
        point.append([x[0], x[1], f(x[0], x[1])])
    return x, point


def draw_plot(point):
    X = point[:, 0]
    Y = point[:, 1]
    Z = point[:, 2]
    fig = plt.figure(figsize=(6, 6))
    ax1 = fig.add_subplot(111, projection="3d")
    x_axis = np.arange(-1, 1, 0.05)
    y_axis = np.arange(-1, 1, 0.05)
    xv, yv = np.meshgrid(x_axis, y_axis)
    z = 5 * xv**2 + yv**2
    mycmap = plt.get_cmap("coolwarm")
    surf1 = ax1.plot_surface(xv, yv, z, cmap=mycmap)
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    ax1.set_zlabel("Z")
    ax1.scatter(X, Y, Z, color="red")
    plt.show()


result, point = GD_fixed_step_size(
    func, gradient_func, init_point, aplha, eps, max_iteration
)
point = np.array(point)
draw_plot(point)

result, point = GD_backtracking_linesearch(
    func, gradient_func, init_point, eps, max_iteration
)
point = np.array(point)
print(point)
draw_plot(point)


def function_3(x):
    return (
        (1.5 - x[0] + x[0] * x[1]) ** 2
        + (2.25 - x[0] + x[0] * (x[1] ** 2)) ** 2
        + (2.625 - x[0] + x[0] * (x[1] ** 3)) ** 2
    )


def GD_backtracking(f, init, max_iter=1000, alpha=1, beta=0.8, tol=1e-4):
    point = []
    x = init
    x_t = x - alpha * nd.Gradient(f)(x)
    for i in range(max_iter):
        if norm(x - x_t) < tol:
            break
        t = 1
        x_t = x - t * alpha * nd.Gradient(f)(x)
        norm_2 = norm(nd.Gradient(f)(x)) ** 2
        f_x = f(x)
        X = x - t * nd.Gradient(f)(x)
        while f(X) > f_x - 1 / 2 * t * alpha * norm_2:
            t *= beta
            X = x - t * alpha * nd.Gradient(f)(x)
        x = X
        point.append([x[0], x[1], f(x)])
    return x, point


A = np.array([1, 1])
x, point = GD_backtracking(function_3, A)
print(f" Cực tiểu của hàm với điểm khởi đầu ({A}):\n x = {x[0], x[1]}")


B = np.array([-4, 3])
x, point = GD_backtracking(function_3, B)
print(f" Cực tiểu của hàm với điểm khởi đầu ({B}):\n x = {x[0], x[1]}")


def newton_backtracking(f, init, alpha=1, beta=0.8, tol=1e-4, max_iter=1000):
    x = init
    point = []
    for i in range(max_iter):
        if norm(x - X) < tol:
            break
        t = 1
        H = nd.Hessian(f)(x)
        G = nd.Gradient(f)(x)
        V = np.linalg.solve(H, G)
        F_x = f(x[0], x[1])
        z = np.dot(G.T, V)
        X = x - alpha * V
        f_x = f(x)
        while f(X) > f_x - 1 / 2 * t * np.linalg.norm(G) ** 2:
            t *= beta
            X = x - t * alpha * V
        x = X
        point.append([x[0], x[1], f(x)])
    return x, point


x, point = newton_backtracking(function_3, A)
print("Phương pháp Newton")
print(f" Cực tiểu của hàm với điểm khởi đầu ({A}):\n x = {x[0], x[1]}")

import gurobipy as gp
from gurobipy import GRB
from gurobipy import quicksum


# (x - y)^2 >= 0 với mọi x, y => min khi x = y
def least_square_opt(x, y):
    N = len(x)
    model = gp.Model()
    a = model.addVar()
    b = model.addVar()

    model.addConstr(
        a * quicksum(x[i] for i in range(N)) + b * N == quicksum(y[i] for i in range(N))
    )

    model.addConstr(
        a * quicksum(x[i] ** 2 for i in range(N)) + b * quicksum(x[i] for i in range(N))
        == quicksum(x[i] * y[i] for i in range(N))
    )

    model.setObjective(0, sense=GRB.MINIMIZE)
    model.optimize()
    for v in model.getVars():
        print(v.varName, v.x)


# Ví dụ minh họa:
x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
print("Bài 4:\n")
least_square_opt(x, y)
