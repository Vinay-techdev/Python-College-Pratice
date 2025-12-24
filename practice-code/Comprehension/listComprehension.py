#square
squares = [x**2 for x in range(5)]
print(squares)

# nested loop
pairs = [ (x, y) for x in [1,2,3] for y in [4,5]]
print(pairs)

matrix = [
    [1,2,3],
    [4,5,6,],
    [7,8,9]
]