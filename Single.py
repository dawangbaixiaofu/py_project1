import pymysql


# 实现链接的单例模式
class Connection(pymysql.connections.Connection):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Connection, cls).__new__(cls)      # 之所以传递cls，是因为__new__是静态方法不是类方法;python可以对静态方法进行重写，java好像不行
        return cls.instance
