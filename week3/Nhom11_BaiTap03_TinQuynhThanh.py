import gurobipy as gp
from gurobipy import GRB


def n_check(n):
    if not type(n) is int:
        return False
    if n <= 0 or (n > 1 and n < 4):
        return False
    return True


def n_queens(n):
    model = gp.Model("N_Queens")

    chess = {}
    for x in range(n):
        for y in range(n):
            chess[x, y] = model.addVar(
                lb=0, ub=1, vtype=GRB.BINARY, name=f"pos[{x}_{y}]"
            )

    model.setObjective(
        gp.quicksum(chess[i, j] for i in range(n) for j in range(n)), GRB.MAXIMIZE
    )

    for i in range(n):
        model.addConstr(gp.quicksum(chess[i, y] for y in range(n)) == 1)
        model.addConstr(gp.quicksum(chess[x, i] for x in range(n)) == 1)

    for k in range(-n + 1, n):
        diagonal = [(x, y) for x in range(n) for y in range(n) if x - y == k]
        model.addConstr(gp.quicksum(chess[x, y] for x, y in diagonal) <= 1)
    for k in range(0, n * 2 - 1):
        diagonal = [(x, y) for x in range(n) for y in range(n) if x + y == k]
        model.addConstr(gp.quicksum(chess[x, y] for x, y in diagonal) <= 1)
    solutions_Count = 0
    while True:
        model.optimize()
        match model.status:
            case GRB.OPTIMAL:
                solutions_Count += 1
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
    print(f"\n Total number of solutions: {solutions_Count}")


n = int(input("Nhập số lượng quân hậu: "))
while n_check(n) == False:
    n = int(input("Nhập lại: "))
n_queens(n)
