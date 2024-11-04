class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def getname(self,name):
        self.name = name
    
    def happybirthday(self,name,age):
        self.name = name
        self.age = age + 1
    

Filip = person("Filip", 23)
Filip.getname("Filip")
Filip.happybirthday("Filip",23)