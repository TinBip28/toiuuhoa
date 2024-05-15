from numpy.linalg import norm
import numpy as np
import matplotlib.pyplot as plt


# Bài tập 2:
def f_2(x, y):
    return 5 * x**2 + y**2


def gradf_2(x, y):
    return np.array([10 * x, 2 * y])


def grad_descent_fixed_step_size(f, gradf, init, alpha, eps, max_iter):
    x_n = init - eps
    x = init
    iter = 0
    point = []
    while norm(x - x_n) > eps and iter < max_iter:
        x_n = x
        x = x - alpha * gradf(x[0], x[1])
        iter += 1
        point.append([x[0], x[1], f(x[0], x[1])])
    return x, point


def grad_descent_adaptive_step_size(f, gradf, init, eps, max_iter):
    x_n = init - eps
    x = init
    iter = 0
    point = []
    while norm(x - x_n) > eps and iter < max_iter:
        alpha = 1
        x_n = x
        norm_2 = norm(gradf(x[0], x[1])) ** 2
        f_x = f(x[0], x[1])
        X = x - gradf(x[0], x[1])
        while f(X[0], X[1]) > f_x - 1 / 2 * alpha * norm_2:
            alpha = 1 / 2 * alpha
            X = x - alpha * gradf(x[0], x[1])
        x = x - alpha * gradf(x[0], x[1])
        iter += 1
        point.append([x[0], x[1], f(x[0], x[1])])
    return x, point


def draw_plot(point):
    X = point[:, 0]
    Y = point[:, 1]
    Z = point[:, 2]
    fig = plt.figure(figsize=(6, 6))
    ax1 = fig.add_subplot(111, projection="3d")
    x_axis = np.arange(-5, 5, 0.1)
    y_axis = np.arange(-5, 5, 0.1)
    xv, yv = np.meshgrid(x_axis, y_axis)
    z = 5 * xv**2 + yv**2
    mycmap = plt.get_cmap("coolwarm")
    surf1 = ax1.plot_surface(xv, yv, z, cmap=mycmap)
    # fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)
    ax1.set_xlabel("X")
    # ax1.set_xlim(-5, 5)
    ax1.set_ylabel("Y")
    ax1.set_zlabel("Z")
    ax1.scatter(X, Y, Z, color="red")
    plt.show()


# Ví dụ minh họa:
print("Bài 2:\n Gradient Descent sử dụng Backtracking line search:")
x, point = grad_descent_adaptive_step_size(f_2, gradf_2, np.array([-4, -4]), 1e-5, 10)
print(point)
point = np.array(point)
print(f" Cực tiểu toàn cục:\n x = {x[0], x[1]}")
draw_plot(point)

print(" Gradient Descent với độ dài bước cố định:")
x, point = grad_descent_fixed_step_size(
    f_2, gradf_2, np.array([-4, -4]), 1e-3, 1e-5, 10
)
point = np.array(point)
print(point)
print(f" Cực tiểu toàn cục:\n x = {x[0], x[1]}")
draw_plot(point)
