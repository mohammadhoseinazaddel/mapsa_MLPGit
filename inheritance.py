class First(object):
    def __init__(self):
        print ("first")

class Second(First):
    def __init__(self):
        print ("second")

class Third(First):
    def __init__(self):
        print ("third")

class Fourth(Second, Third):
    def __init__(self):
        # super(Third,self).__init__()
        Third.__init__(self)
        print ("that's it")

print(isinstance(object,object))
print(issubclass(object,object))
print(isinstance(type,type))
print(issubclass(type,type))
print(issubclass(type,str))
Fourth()