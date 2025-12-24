
def isVowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in s:
        if ch in vowels:
            count+=1
    return count

str = input("Enter string: ")
count = isVowels(str)
if(count >0):
    print(f"String '{str}' contains vowels, vowels count: {count}")
else:
    print(f"string '{str}' does not conatian vowels")
