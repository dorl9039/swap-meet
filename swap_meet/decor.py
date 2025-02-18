from .item import Item

class Decor(Item):
    
    def __init__(self, age=0, id=None, condition=0, width=0, length=0):
        super().__init__(age, id, condition)
        self.width = width
        self.length = length
    
    
    def get_category(self):
        return "Decor"
    
    
    def __str__(self):
        line1 = super().__str__()
        line2 = f"It takes up a {self.width} by {self.length} sized space."
        return " ".join((line1, line2))