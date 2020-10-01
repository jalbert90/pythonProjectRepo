#!/usr/bin/python3

class Position:
    posCounter = 0

    def __init__(self, ticker, prices, quantities):
        self.ticker = ticker
        self.prices = prices
        self.quantities = quantities
        Position.posCounter += 1 

    def incPos(self, price, quantity):
        self.prices.append(price)
        self.quantities.append(quantity)
    
    def undoIncPos(self):
        self.prices.pop(len(self.prices) - 1)
        self.quantities.pop(len(self.quantities) - 1)

    def decPos(self, quantity):
        sellCounter = 0
        while sellCounter < quantity:
            if self.quantities[0] > 1:
                self.prices[0] -= self.prices[0] / self.quantities[0]
                self.quantities[0] -= 1
                sellCounter += 1
            else:
                self.prices.pop(0)
                self.quantities.pop(0)
                sellCounter += 1

    def getPosPrinciple(self):
        sum = 0
        for i in range(0, len(self.prices)):
            sum += self.prices[i] * self.quantities[i]
        return sum

    def getPosQuantity(self):
        quan = 0
        for i in self.quantities:
            quan += i
        return quan

    def getAvgPrice(self):
        return self.getPosPrinciple() / self.getPosQuantity()

    def getPLOpen(self, mark):
        return (mark - self.getAvgPrice()) * self.getPosQuantity()

    def getPLOpenPercent(self, mark):
        return (self.getPLOpen(mark) / self.getPosPrinciple()) * 100
