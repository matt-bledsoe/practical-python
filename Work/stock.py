# Stock class
import typedproperty

class Stock:
    # __slots__ = ("name", "shares", "price")
    name = typedproperty.String("name")
    shares = typedproperty.Integer("shares")
    price = typedproperty.Float("price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def __repr__(self) -> str:
        return f"Stock:('{self.name}', {self.shares}, {self.price})"
    
    @property
    def cost(self):
        return self.shares * self.price
    
    def sell(self, shares_sold):
        self.shares -= shares_sold

