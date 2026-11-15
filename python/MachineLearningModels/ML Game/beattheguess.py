import scipy
import numpy as np
from sklearn.linear_model import LinearRegression
def guess():
    user_input = int(input("enter a number between 1 and 100:"))
    run= True
    while run == True:
        try:
            if user_input ==int and user_input > 1 and user_input < 100:
                arr = []
                print ("sucess")
                CHOICE = str(input("again?"))
                if user_input == "y":
                    arr.append(user_input)
                    guess()
        except ValueError:
            print ("please insert correct number")
            guess()
            
            continue

guess()