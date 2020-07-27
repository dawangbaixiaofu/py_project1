class Single:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'instance'):
            cls.instance = super(Single, cls).__new__(cls)
        return cls.instance
s = Single()
print(s)
s1 = Single()
print(s1)