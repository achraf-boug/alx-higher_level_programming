#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        str = ""
        if i % 3 == 0:
            str+= "Fizz"
        if i % 5 == 0:
            str+= "Fizz"
        print("{} {}".format(i,str), end=" ")
