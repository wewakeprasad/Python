class Student(object):
    #Initializer
    def __init__(self,name):
        # An instance variale to hold the stduent's name
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,new_name):
        self._name = new_name

bob = Student("Bob")
print(bob.name)
bob.name = "Alice"
print("Changed Name",bob.name)

