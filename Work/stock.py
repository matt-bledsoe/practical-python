# Stock class

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def __repr__(self) -> str:
        return f"Stock:('{self.name}', {self.shares}, {self.price})"
    def cost(self):
        return self.shares * self.price
    
    def sell(self, shares_sold):
        self.shares -= shares_sold

