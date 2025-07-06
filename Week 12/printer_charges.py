def calculate_charge(x):

    if x <= 100:
        return x*0.03
    elif x <= 300:
        return (100*0.03)+((x-100)*0.02)
    else:
        return (100*0.03)+(200*0.02)+((x-300)*0.01)
    
def calculate_gst(x):

    return x + (x*0.09)


print("{:<5}   {:>10}   {:>15}".format("Pages","Charge($)","Include gst($)"))

for y in range(0,501,50):

    print('{:<5}   {:>10.2f}   {:>15.2f}'.format(y,calculate_charge(y),calculate_gst(calculate_charge(y))))
