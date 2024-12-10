
arr1 = []
with open("molpy.txt","r") as file:
    for i in file:
        arr1.append(i.rstrip())
    file.close()

arrhead = []
for i in range(1):
    arrhead.append(arr1[i])
arr2 = []
for i in range(1, len(arr1)):
    arr2.append(arr1[i])

arr3 = []

for i in arr2:
    list1 = i.split(" ")
    while True:
        if "" in list1:
            list1.remove("")
        if "" not in list1:
            break
    if len(list1) == 4:
        arr3.append(list1)


irred_list = []       #[A',A'']
index_list = []       #[[1,2],[3,4,5]]
index_length = []    #[2,3]
for i in arr3:
    if i[-1] not in irred_list:
        irred_list.append(i[-1])
for i in range(len(irred_list)):
    sub_list = []
    index_list.append(sub_list)
for i in range(len(arr3)):
    irred = arr3[i][-1]
    index = irred_list.index(irred)
    index_list[index].append(i)

for i in index_list:
    index_length.append(len(i))

#need to print this into supsym format

print(irred_list)
print(index_list)
print(index_length)        

str_index_length = [str(x) for x in index_length]
str_index_list = []
for x in index_list:
    i = 0
    while i <= len(x):
        str_index = "            "
        if (len(x) - i) >= 10 :
            sub = 10    #print by 4 elements at a time
        else:
            sub = (len(x) - i)
        j = 0
        while j < sub:
            str_index += "  " + str(x[i+j]+1) + " "  
            j+=1
        print(str_index)
        i += 10
        str_index_list.append(str_index)
 
print(str_index_list)

with open("supsym.txt","w") as file2:
    for i in str_index_list:
        file2.write(i + "\n")
    file2.close
    

