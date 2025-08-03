class bikeshop:
    def __init__(self,stock):
        self.stock=stock
    def displaystock(self):
        print("Total Bike",self.stock)
    def rentbike(self,q):

        if q <=0:
            print("please enter the value grater than 1")
        elif q > self.stock:
            print("Please enter the value accoung tho tha available stock")
        else:
            self.stock = self.stock - q
            print("Total price",q*100)
            print("Available stock",self.stock)

while True:
    obj = bikeshop(100)
    uc = int(input('''
1. display stock
2. rent a bike
3. exit
    '''))

    if uc == 1:
        obj.displaystock()
    elif uc == 2:
        n = int(input("Enter the quantity:--"))
        obj.rentbike(n)
    else:
        break