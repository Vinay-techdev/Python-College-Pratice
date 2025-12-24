
def maxMin():
    list=[10, 20, 30, 40]
    max = list[0]
    min = list[0]

    for i in list:
        if(i>max):
            max=i
        
        if(i<min):
            min=1
    print("max: ",max)
    print("min: ",min)

maxMin()