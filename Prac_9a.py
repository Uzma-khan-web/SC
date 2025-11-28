#Aim: Find the ratios using Fuzzy Logic
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

s1 = "I love fuzzyforfuzzys"
s2 = "I am loveing fuzzyforfuzzys"

print("\nFuzzywuzzy Ratio:", fuzz.ratio(s1, s2))
print("\nFuzzywuzzy Partial Ratio:", fuzz.partial_ratio(s1, s2))
print("\nFuzzywuzzy Token Sort Ratio:", fuzz.token_sort_ratio(s1, s2))
print("\nFuzzywuzzy Token Set Ratio:", fuzz.token_set_ratio(s1, s2))
print("\nFuzzywuzzy WRatio:", fuzz.WRatio(s1, s2))

query = 'fuzzy for fuzzys'
choices = ['fuzzy for fuzzy', 'fuzzy fuzzy', 'g. for fuzzys']

print("\nList of ratios:")
print(process.extract(query, choices), '\n')

print("Best match from list:", process.extractOne(query, choices))
