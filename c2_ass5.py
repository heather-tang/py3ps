
olympics = 'Beijing', 'London', 'Rio', 'Tokyo'



tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]

country = []
for tup in tuples_lst:
    country.append(tup[1])
    
     

olymp = ('Rio', 'Brazil', 2016)

city, country, year = olymp



def info(name, gender, age, bday_month, hometown):
    return name, gender, age, bday_month, hometown
    
      

gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}

num_medals = []
for c,m in gold.items():
    num_medals.append(m)
