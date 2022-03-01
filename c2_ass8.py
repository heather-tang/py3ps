letters = "alwnfiwaksuezlaeiajsdl"
lst = []
for char in letters:
    lst.append(char)
sorted_letters = sorted(lst, reverse = True)



animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']

animals_sorted = sorted(animals)




medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
y = sorted(medals.keys())
alphabetical = []
for country in y:
    alphabetical.append(country)
    
    
    

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

top_three = sorted(medals, key = lambda k: medals[k], reverse = True)[:3]




groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

most_needed = sorted(groceries, key = lambda k: groceries[k], reverse = True)



def last_four(x):
    return str(x)[-4:]

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids = sorted(ids, key = last_four)




ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_id = sorted(ids, key = lambda end: str(end)[-4:])




ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

lambda_sort = sorted(ex_lst, key = lambda i: i[1])
