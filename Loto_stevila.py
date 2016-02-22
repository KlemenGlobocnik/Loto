from random import randint

def lot_stevila(x,a,b):
    prices = []
    while len(prices)<x:
        y=randint(a,b)  # y = 5
        if y not in prices:
            prices.append(y)
    return prices

def main():
    print lot_stevila(5,1,1000)

if __name__=="__main__":
    main()

