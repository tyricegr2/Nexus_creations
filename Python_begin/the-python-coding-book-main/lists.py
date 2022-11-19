
nirvana = "Nirvana"
eon = "Eon"
uzar = "Uzar"
socrates = "Socrates"

nexus = [nirvana, eon, uzar, socrates]

correlated_bs = ["thought", 42, True, "bye bye", nirvana, 1, 1, 2, 3, 5, 8, 13, 21, 34]

print(correlated_bs[1:3])
print(correlated_bs[-2])

# below indicates slicing from index 2 through 12 with increments of 2 indices 
# or step size of 2

print(correlated_bs[2:12:2])

# slicing in other ways 


print(correlated_bs[:7]) # prints everything up to and exluding 7th indice
print(correlated_bs[4:]) # prints everything after 4th indice

# Reversing a list
print(correlated_bs[::-1])

for archetype in nexus:
    print(f"Hello {archetype}. What's our goals today?")

upper_case_names = [name.upper() for name in nexus]
print(upper_case_names)
