def fsequence(x,z):
    print(x)
    y = 0
    sum = x
    while y < z: 
        sum = x + sum
        x = sum - x
        print(sum) 
        y +=1

fsequence(1,9)
