x = int(input("Input N : "))
for i in range(x):
    data = []
    for j in range(x):
        data.append((i+j)%5+1)
    print(data)