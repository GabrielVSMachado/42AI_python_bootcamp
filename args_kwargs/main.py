class ObjectC(object):
    def __init__(self, *args, **kwargs):
        for position, value in enumerate(args):
            self.__setattr__("var_" + str(position), value)
        self.__dict__.update(**kwargs)


def what_are_the_vars(*args, **kwargs) -> ObjectC:
    obj = ObjectC(*args, **kwargs)
    if len(obj.__dict__) < len(args) + len(kwargs):
        del obj
        return None
    return obj


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", var_0="hello")
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", var_2="hello")
    doom_printer(obj)
