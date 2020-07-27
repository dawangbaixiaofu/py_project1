from datetime import datetime

class medicine():
    def __init__(self,name,price,pd,exp):
        self.name = name
        self.price = price
        self.pd = pd
        self.exp = exp
    def get_price(self,price=self.price):
        return price
    def get_name(self):
        return self.name
    def get_gp(self):
        start = datetime.strptime(self.pd,'%Y-%m-%d')
        end = datetime.strptime(self.exp,'%Y-%m-%d')
        GP = end-start
        return GP.days
    def is_expire(self):
        now = datetime.now()
        end = datetime.strptime(self.exp,'%Y-%m-%d')
        if now > end:
            return False
        else:
            return True
if __name__ == '__main__':
    medicineObject = medicine('感冒胶囊',100,'2019-1-1','2020-1-1')
    print('药名是：',medicineObject.get_name())
    print('药的价格是：',medicineObject.get_price())
    print('药的保持期：',medicineObject.get_gp())
    print("药是否过期：",medicineObject.is_expire())


