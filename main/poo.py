

class TheSimplestClass:
    pass
 
my_first_object = TheSimplestClass()


class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)


class ExampleClassTwo:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClassTwo.counter += 1


example_object_1 = ExampleClassTwo()
example_object_2 = ExampleClassTwo(2)
example_object_3 = ExampleClassTwo(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

class ExampleThree:
    varia = 1
    def __init__(self, val):
        ExampleThree.varia = val


print(ExampleThree.__dict__)
example_object = ExampleThree(2)

print(ExampleThree.__dict__)
print(example_object.__dict__)
    
class ExampleClassFour:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClassFour(1)
print(example_object.a)

if hasattr(example_object, 'b'):
    print(example_object.b)