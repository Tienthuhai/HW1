class Cup:
    def __init__(self, size:int , quantity:int ):
        self.size = size
        self.quanity = quantity

    def fill(self,milimeters):
        if self.size - self.quanity >= milimeters:
            self.quanity += milimeters
        else:
            return
        
    def status(self):
        return self.size - self.quanity
    

