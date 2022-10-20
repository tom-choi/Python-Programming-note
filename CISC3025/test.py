
for i in range(1,50):
    print(i%(12 + (i > 12 if 1 else 0))+1+(i >= 12 if 1 else 0))