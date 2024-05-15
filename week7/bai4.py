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
