# MAT2407-MT (T3 & T5) group 11
# Beale function. f(x_1,x_2) = (1.5 - x_1 + x_1 x_2)^2 + (2.25 - x_1 + x_1 x_2^2)^2 + (2.625 - x_1 + x_1 x_2^3)^2
# Points A(0,0) and B(-4,3).
import numpy as np
from numpy.linalg import norm
import numdifftools as nd
import matplotlib.pyplot as plt


def function(x):
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
x, point = GD_backtracking(function, A)
print(f" Cực tiểu của hàm với điểm khởi đầu ({A}):\n x = {x[0], x[1]}")


B = np.array([-4, 3])
x, point = GD_backtracking(function, B)
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
        X = x - np.linalg.inv(H) @ G
        X = x - t * np.linalg.inv(H) @ G
        f_x = f(x)
        while f(X) > f_x - 1 / 2 * t * np.linalg.norm(G) ** 2:
            t *= beta
            X = x - t * np.linalg.inv(H) @ G
        x = X
        point.append([x[0], x[1], f(x)])
    return x, point
