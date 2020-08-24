from pyomo.environ import *
from pyomo.opt import SolverFactory
# create a model
model = ConcreteModel()

# declare decision variables
model.x = Var(domain=pyomo.environ.NonNegativeReals) # NonNegativeReals代表非0实数
model.y = Var(domain=pyomo.environ.NonNegativeReals)

# declare objective
model.profit = Objective(expr = 40*model.x + 30*model.y, sense=maximize)

# declare constraints
model.demand = Constraint(expr = model.x <= 40)
model.laborA = Constraint(expr = model.x + model.y <= 80)
model.laborB = Constraint(expr = 2*model.x + model.y <= 100)

model.pprint()


# 求解模型
# GLPK全称GNU Linear Programming Kits，是GNU opensource 的用于解
# 线性规划的项目，功能非常强大，对于一般的线性规划问题只需给出目标函数和各种约束，就能自动运算得出正确解。
# 需要自己进行下载安装
SolverFactory("glpk").solve(model).write()
# display solution
print('\nProfit = ', model.profit())


print('\nDecision Variables')
print('x = ', model.x())
print('y = ', model.y())


print('\nConstraints')
print('Demand  = ', model.demand())
print('Labor A = ', model.laborA())
print('Labor B = ', model.laborB())