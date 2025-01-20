class father:        # parent class in inheritance
    name = "imran"
    age = "44"
    def height(self):
        print("he is very tall")

    def looks(self):
        print("he is very klug")

class child1(father): # child class in inheritance
    def weight(self):
        print("his weight is 70 kg")
        # we can call super as parent class as well.. father is parent class and we are calling super() as well. 
        print("calling variables " + super().age + " and " + father.name)

        def __str__(self): # str functions use when nothing is called . so str will be called by default 
            return "Hello Ali"
        # Starting multiple inheritance

c1 = child1()
c1.height()
c1.looks()
c1.weight()