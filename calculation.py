class Operator():
    numberA = 0.0
    numberB = 0.0
    result = 0.0
    def get_result(self):
        return self.result

class OperationAdd(Operator):
    def get_result(self):
        self.result = self.numberA+self.numberB
        return self.result

class OperationSub(Operator):
    def get_result(self):
        self.result = self.numberA - self.numberB
        return self.result

class OperationMul(Operator):
    def get_result(self):
        self.result = self.numberA*self.numberB
        return self.result
class OperationDiv(Operator):
    def get_result(self):
        self.result = self.numberA/self.numberB
        return self.result

class OpeFactory():
    @staticmethod
    def createOperate(operate):
        optList = {
            "+":OperationAdd,
            "-":OperationSub,
            "*":OperationMul,
            "/":OperationDiv
        }
        oper = Operator()
        if(operate in optList):
            oper = optList[operate]()
        return oper

if __name__ == '__main__':
    numberA = 3
    numberB = 4
    oper = OpeFactory.createOperate("+")
    oper.numberA = numberA
    oper.numberB = numberB
    print(oper.get_result())