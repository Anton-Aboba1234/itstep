class BaseClass:

   def __init__(self, base_attr):
       self.base_attr = base_attr
   def base_method(self):
       print("Metod Base class")

class ChildClass1(BaseClass):
   def __init__(self, base_attr, child1_attr):
       super().__init__(base_attr)
       self.child1_attr = child1_attr
   def child1_method(self):
       print("Metod I child class")


class ChildClass2(BaseClass):
   def __init__(self, base_attr, child2_attr):
       super().__init__(base_attr)
       self.child2_attr = child2_attr
   def child2_method(self):
       print("Metod II child class")

obj1 = ChildClass1("attribute base class", "attribute I child class")
obj2 = ChildClass2("attribute base class", "attribute II child class")

obj1.base_method()
obj1.child1_method()
print(obj1.base_attr)
print(obj1.child1_attr)
obj2.base_method()
obj2.child2_method()
print(obj2.base_attr)
print(obj2.child2_attr)