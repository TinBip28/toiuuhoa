import itertools
import gurobipy as gp
from gurobipy import GRB
import numpy as np

model = gp.Model("Ten chuong trinh")

x_1 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="foo")
x_2 = model.addVar(lb=0, vtype=GRB.CONTINUOUS)
x_3 = model.addVar(lb=0, vtype=GRB.CONTINUOUS)

model.addConstr(x_1 <= 0)
model.addConstr(x_2 <= 5)
model.addConstr(x_3 <= 2)
model.addConstr(4 * x_1 + x_2 + x_3 <= 25)

model.setObjective(2 * x_1 + x_2 + 2 * x_3, sense=G yRB.MAXIMIZE)
model.optimize()
