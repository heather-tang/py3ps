
def sublist(list):
    n = 0
    new_list = []
    while n < len(list) and list[n] != 5:
        new_list.append(list[n])
        n = n + 1
    return new_list
  
  
  

def check_nums(list):
    n = 0
    new_list = []
    
    while n < len(list) and list[n] != 7:
        new_list.append(list[n])
        n = n + 1
    
    return new_list
  
  
  

def sublist(list):
    n = 0 
    n_list = []
    
    while n < len(list) and list[n] != 'STOP':
        n_list.append(list[n])
        n = n + 1
    return n_list
  
  
  
  
def stop_at_z(list):

    n = 0
    n_list = []
    
    while n < len(list) and list[n] != 'z':
        n_list.append(list[n])
        n = n + 1
    return n_list 
  
  
  

sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x

sum2 = 0
n = 0
while n < len(lst):
    sum2 = sum2 + lst[n]
    n = n + 1
    
    
    

def beginning(list):
    n = 0
    n_list = []
    
    if len(list) > 10:
        max = 10
    else: 
        max = len(list)
    
    while n <= (max-1) and list[n] != 'bye':
        n_list.append(list[n])
        n = n + 1
    return n_list
        
    #if len(n_list) > 10:
    #    return n_list[:10]
    #else:
    #    return n_list
