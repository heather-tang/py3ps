Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for akey in Junior:
    credits += Junior[akey] 
    
    
    
str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for char in str1:
    if char not in freq:
        freq[char] = 0
    freq[char] = freq[char] + 1
 
 
 
s1 = "hello"

counts = {}
for char in s1:
    if char not in counts:
        counts[char] = 0
    counts[char] += 1
    
    
    
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"

freq_words = {}
for word in str1.split():
    if word not in freq_words:
        freq_words[word] = 0
    freq_words[word] += 1
    
    
    
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"

wrd_d = {}
for word in sent.split():
    wrd_d[word] = wrd_d.get(word, 0) + 1
    
    
    
sally = "sally sells sea shells by the sea shore"

characters = {}
for char in sally:
        characters[char] = characters.get(char, 0) + 1
print(characters)
    
cks = characters.keys()
best_char = list(cks)[0]
for akey in cks:
    if characters[akey] > characters[best_char]:
        best_char = akey
        
        
        
sally = "sally sells sea shells by the sea shore and by the road"

characters = {}
for char in sally:
    characters[char] = characters.get(char, 0) + 1

dks = characters.keys()
worst_char = list(dks)[0]
for akey in dks:
    if characters[akey] < characters[worst_char]:
        worst_char = akey 
        
        
        
string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."

letter_counts = {}
for char in string1.lower():
    letter_counts[char] = letter_counts.get(char, 0) + 1
    
    
    
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."

low_d = {}
for char in p.lower():
    low_d[char] = low_d.get(char, 0) + 1

    
