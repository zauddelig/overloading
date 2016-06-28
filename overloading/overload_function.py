import inspect
from functools import wraps

class AbsOverload:
    pass

def overload(overloaded):

    class Wrapper(AbsOverload):
        __slots__ = ("__data", )

        def __init__(self):
            self.__data = []

        def register(self, overloading):
            self.__data.append(overloading)
            return self

        def __call__(self, *args, **kwargs):
            for func in self.__data:
                args_spec = inspect.getfullargspec(func)

        pass
    return Wrapper()

