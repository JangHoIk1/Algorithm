array = [4,2,1,7,5]

for i in range(len(array)):

    min_index=i


    for j in range(i+1,len(array)):

        if array[min_index]>array[j]:
            array[min_index],array[j]=array[j],array[min_index]



print(array)
