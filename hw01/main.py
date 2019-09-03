for i in range(1,10):
    for j in range(1,i):
        print(f'        ',end=" ")
    for j in range(i,10):
        print(f"{i:2d}X{j:<2d}={i*j:2d}",end=" ")
    
    print('')
