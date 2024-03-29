from gurobipy import *


# create a model
m = Model()

# create variables
x16 = m.addVar(vtype=GRB.CONTINUOUS, name="x16", lb=0)
x17 = m.addVar(vtype=GRB.CONTINUOUS, name="x17", lb=0)
x18 = m.addVar(vtype=GRB.CONTINUOUS, name="x18", lb=0)
x19 = m.addVar(vtype=GRB.CONTINUOUS, name="x19", lb=0)
x26 = m.addVar(vtype=GRB.CONTINUOUS, name="x26", lb=0)
x27 = m.addVar(vtype=GRB.CONTINUOUS, name="x27", lb=0)
x28 = m.addVar(vtype=GRB.CONTINUOUS, name="x28", lb=0)
x29 = m.addVar(vtype=GRB.CONTINUOUS, name="x29", lb=0)
x36 = m.addVar(vtype=GRB.CONTINUOUS, name="x36", lb=0)
x37 = m.addVar(vtype=GRB.CONTINUOUS, name="x37", lb=0)
x38 = m.addVar(vtype=GRB.CONTINUOUS, name="x38", lb=0)
x39 = m.addVar(vtype=GRB.CONTINUOUS, name="x39", lb=0)
x46 = m.addVar(vtype=GRB.CONTINUOUS, name="x46", lb=0)
x47 = m.addVar(vtype=GRB.CONTINUOUS, name="x47", lb=0)
x48 = m.addVar(vtype=GRB.CONTINUOUS, name="x48", lb=0)
x49 = m.addVar(vtype=GRB.CONTINUOUS, name="x49", lb=0)
x56 = m.addVar(vtype=GRB.CONTINUOUS, name="x56", lb=0)
x57 = m.addVar(vtype=GRB.CONTINUOUS, name="x57", lb=0)
x58 = m.addVar(vtype=GRB.CONTINUOUS, name="x58", lb=0)
x59 = m.addVar(vtype=GRB.CONTINUOUS, name="x59", lb=0)


# integrate new variables
m.update()

# set objective
m.setObjective(
    541.0*x16 + 386.0*x17 + 25.0*x18 + 1512.0*x19 + 234.0*x26 + 899.0*x27 + 103.0*x28 + 1256.0*x29 + 543.0*x36 + 257.0*x37 + 1653.0*x38 + 1085.0*x39 + 1785.0*x46 + 227.0*x47 + 1670.0*x48 + 823.0*x49 + 490.0*x56 + 1233.0*x57 + 1242.0*x58 + 1841.0*x59,
    GRB.MINIMIZE
)

# add constraints
m.addConstr(x16 + x17 + x18 + x19 == 208.0)
m.addConstr(x26 + x27 + x28 + x29 == 193.0)
m.addConstr(x36 + x37 + x38 + x39 == 195.0)
m.addConstr(x46 + x47 + x48 + x49 == 209.0)
m.addConstr(x56 + x57 + x58 + x59 == 4031.0)
m.addConstr(-1*(x16 + x26 + x36 + x46 + x56) == -1530.0)
m.addConstr(-1*(x17 + x27 + x37 + x47 + x57) == -1583.0)
m.addConstr(-1*(x18 + x28 + x38 + x48 + x58) == -1562.0)
m.addConstr(-1*(x19 + x29 + x39 + x49 + x59) == -161.0)
m.addConstr(x16 <= 7407.0 + 0.0)
m.addConstr(x17 <= 3546.0 + 0.0)
m.addConstr(x18 <= 5072.0 + 0.0)
m.addConstr(x19 <= 1932.0 + 0.0)
m.addConstr(x26 <= 81.0 + 0.0)
m.addConstr(x27 <= 90.0 + 0.0)
m.addConstr(x28 <= 29.0 + 144.0)
m.addConstr(x29 <= 902.0 + 0.0)
m.addConstr(x36 <= 13.0 + 0.0)
m.addConstr(x37 <= 8413.0 + 0.0)
m.addConstr(x38 <= 8719.0 + 0.0)
m.addConstr(x39 <= 7439.0 + 0.0)
m.addConstr(x46 <= 5047.0 + 0.0)
m.addConstr(x47 <= 83.0 + 0.0)
m.addConstr(x48 <= 58.0 + 0.0)
m.addConstr(x49 <= 76.0 + 0.0)
m.addConstr(x56 <= 83.0 + 1372.0)
m.addConstr(x57 <= 7904.0 + 0.0)
m.addConstr(x58 <= 73.0 + 855.0)
m.addConstr(x59 <= 65.0 + 0.0)

# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)