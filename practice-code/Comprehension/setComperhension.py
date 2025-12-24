
num = [1,2,3,4,5,6,7,8]
squares = {n*n for n in num if n%2==0}
print(squares)

words = ["hello", "world", "python"]
upper = {word.upper() for word in words }
print(upper)

set1 = {1,2,3,4}
set2 = {3,4,5,6}

union = {(u, w) for u in set1 for w in set2 }
print(union)

sen = "The cat in the hat had two sidekicks, thing one and thing two."
un_word = sen.lower().replace(',', "").replace('.', "").split()
sents = {s for s in un_word}
print(sents)

sentance =  "The cat in the hat had two sidekicks, thing one and thing two."
words = sen.lower().replace(',', "").replace('.', "").split()

vowels = ['a', 'e','i','o','u']
fz = {frozenset([letter for letter in words if letter == vowels])}
print(fz)
