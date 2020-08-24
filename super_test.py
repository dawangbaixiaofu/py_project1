class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')


class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')

    @classmethod
    def test(cls):
        print('this is a class method')



class C(Base):
    def __init__(self):
        super().__init__()
        print('C.__init__')


class D(A, B, C):
    def __init__(self):
        super(A, D).test()  # 等同于 super(D, self).__init__()
        print('D.__init__')

    def test_method(self, n):
        print('this is instance method and the n is:',n)


D()
print(D.test_method(D(),2))
# super(type,[object,type2]).method()
# super()返回值是一个object的mro表（即object继承类列表，是按照继承顺序排列的）中type类的下一个类；
# MRO（method resolution order）
