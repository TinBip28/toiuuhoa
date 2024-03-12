import itertools
import gurobipy as gp
from gurobipy import GRB
import numpy as np

model = gp.Model("Ten mo hinh")
x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="foobar")
y = model.addVar(lb=0, vtype=GRB.CONTINUOUS)

model.addConstr(x + y == 5)
model.addConstr(4 * x + y <= 11)

model.setObjective(2 * x + y, sense=GRB.MAXIMIZE)
model.optimize()
