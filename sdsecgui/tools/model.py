# _*_coding:utf-8_*_
class SingletonInstane:
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def getInstance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.getInstance = cls.__getInstance
        return cls.__instance