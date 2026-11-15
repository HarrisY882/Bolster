import scipy
import numpy as np
from sklearn.linear_model import LinearRegression
def guess():
    user_input = input("enter a number between 1 and 100:")
    run= True
    while run == True:
        try:
            if user_input.isdigit() and user_input > 1 and user_input < 100:
                pass
        except ValueError:
            guess()
            continue

guess()