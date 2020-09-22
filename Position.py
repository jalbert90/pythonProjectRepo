#!/usr/bin/python3

class Position:
    positonCounter = 0

    def __init__(self, ticker, price, quantity):
        self.ticker = ticker
        self.price = [price]
        self.quantity = [quantity]
        positionCounter += 1 

    def increasePosition(self, price, quantity):
        self.price.append(price)
        self.quantity.append(quantity)

    def decreasePositon(self, quantity):
        sellCounter = 0
        while sellCounter < quantity:
            if self.quantity[0] > 1:
                self.price[0] -= self.price[0] / self.quantity[0]
                self.quantity[0] -= 1
                sellCounter += 1
            else:
                self.price.pop(0)
                self.quantity.pop(0)
                sellCounter += 1

    def getPositonPrinciple(self):
        sum = 0
        for i in price:
            sum += i
        return sum

    def getPositionQuantity(self):
        quan = 0
        for i in quantity:
            quan += i
        return quan

    def getAveragePrice(self):
        return self.getPositionPrinciple() / self.getPositionQuantity
