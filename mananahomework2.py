from __future__ import division
our_list= input ("Input some numbers seprated by a comma: ")
def avg(our_list):
    return sum(our_list) / len(our_list)
print avg(our_list)
from __future__ import division
our_list2= input ("Input some numbers seprated by a comma: ")
number_of_occurrances = input ("Inpute the number of occurrences")
def avg(our_list2):
    return sum(our_list2[len(our_list2)-number_of_occurrances:])/number_of_occurrances
print avg(our_list2)
import random
number=random.randint(1,100)
print number
def game(number):
    if number > 50 and number < 100:
        return "WIN"
    elif number ==100:
        return "DRAW"
    elif number >=1 and number <=50 :
        return "Loss"
print game (number)
import pandas_datareader.data as web
our_list3=[web.DataReader("DIS","google"),web.DataReader("TSLA","google"),web.DataReader("SBUX","google")]
for x in our_list3:
    print x.head(7)
    import matplotlib.pyplot as plt
    for x in our_list3:
    plt.plot(x)
    plt.show()