def asc(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] < data[j]:
                data[i],data[j] = data[j],data[i]
    return data

list1 = [67,45,2,13,1,998]
list2 = [89,23,33,45,10,12,45,45,45]

print(asc(list1))
print(asc(list2))

    
