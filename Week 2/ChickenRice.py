#Ang Hao Yi 10273989D

import math

priceofchickenrice = float(input('Kindly enter price of chicken rice '))
additionalsidedishes = int(input('Kindly enter the number of additional side dishes '))

pricetotaldishes = 1.2*additionalsidedishes

totalcostwithouttax = priceofchickenrice + pricetotaldishes
totalcostwithtax = totalcostwithouttax + (totalcostwithouttax*0.09)

def roundtonearest1(value):
    return math.ceil(value*10)/10
print('Total cost of the purchase is $',roundtonearest1(totalcostwithtax))