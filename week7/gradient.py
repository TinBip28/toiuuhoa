import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt


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
