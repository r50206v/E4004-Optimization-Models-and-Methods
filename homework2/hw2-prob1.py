from gurobipy import *


# create a model
m = Model("problem 1")

# create variables
# xi, j := represents method i for j product (gas or heating oil)
x1 = m.addVar(vtype=GRB.CONTINUOUS, name="x1", lb=0)
x2 = m.addVar(vtype=GRB.CONTINUOUS, name="x2", lb=0)
x3 = m.addVar(vtype=GRB.CONTINUOUS, name="x3", lb=0)
x4 = m.addVar(vtype=GRB.CONTINUOUS, name="x4", lb=0)
x5 = m.addVar(vtype=GRB.CONTINUOUS, name="x5", lb=0)
x6 = m.addVar(vtype=GRB.CONTINUOUS, name="x6", lb=0)


# integrate new variables
m.update()

# set objective
m.setObjective(
    2*x1 - x2 + x3,
    GRB.MAXIMIZE
)

# add constraints 
m.addConstr(3*x1 + x2 + x3 + x4 == 60)
m.addConstr(x1 - x2 + 2*x3 + x5 == 10)
m.addConstr(x1 + x2 - x3 + x6 == 20)

# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)
