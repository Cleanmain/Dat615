class Doorlock:
    def __init__(self,pin):
        self.pin = pin
        self.locked = False

    def lock(self):
        if self.locked == False:
            self.locked = True
            return True
        else:
            return False
        
    def unlock(self,pin):
        if self.pin == pin and self.locked == True:
            self.locked = False
            return True
        else:
            return False
        
    def set_pin(self,pin,new_pin):
        if self.locked == False and self.pin == pin:
            self.pin = new_pin
            return True
        else:
            return False
    
mylock = Doorlock(1234)
mylock.lock()
mylock.unlock(1234)
mylock.set_pin(1234,5555)
