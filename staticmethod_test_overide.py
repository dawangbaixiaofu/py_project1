class Test:
    @staticmethod
    def test():
        print('this is a test!')


class Test1(Test):
    @staticmethod
    def test():
        super(Test1, Test1).test()
        print('this is a test1!')


if __name__ == '__main__':
    t = Test1()
    t.test()