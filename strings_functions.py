# length function returns the amount of the given word
def length(st):
    list_st = list()
    quantity = 0
    for i in st:
        list_st.extend(i)
        quantity += 1
    return quantity

# name function returns the given word   
def name(st):
    return st

# testing the function
a = length('words')
name = name("words")
print(f"the amount of words in '{name}' is {a}")
print()

# Unique_symb function returns a number of unique symbols in a given word

def unique_symb(st):
    st_dict = {}
    for i in st:
        keys = st_dict.keys()
        if i in keys:
            st_dict[i] += 1
        else:
            st_dict[i] = 1
    return st_dict
    
# testing the function
print(unique_symb("scoobie doo"))

# rang function returns a sequence of numers (integers) from n1 (including) to n2 (not including) with step n3 
def rang(n2, n1 = 0, n3 = 1):
    l = list()
    while n1 < n2:
        l.append(n1)
        n1 += n3
    return l

# testing the function
a = range(1,5,2)
print(f"function range(1,5,2) : {a}")
print(f"created function rang(5, 1, 2) : {rang(5, 1, 2)}")






