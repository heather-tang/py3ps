
def mult(a, b=6):
    return a*b
    
    
    

def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))




def sum(intx, intz=5):
    return intz + intx




def test(a, b=True, dict1={2:3, 4:5, 6:8}):
    if b is True:
        if a in dict1.keys():
            return dict1[a]
    else:
        return False




def checkingIfIn(a, direction=True, d={'apple':2, 'pear':1, 'fruit':19, 'orange':5, 'banaba':3, 'grapes':2, 'watermelon':7}):
    if direction is True:
        if a in d.keys():
            return True
        else:
            return False
    else:
        if a not in d.keys():
            return True
        else:
            return False
            
            
            

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]




def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn('lime')
# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn('papaya', False)
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans = checkingIfIn('fruit')
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn('orange') + checkingIfIn('banana')

