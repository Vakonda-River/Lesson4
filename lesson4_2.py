lst = [300,2,12,44,1,1,4,10,7,1,78,123,55]
print('Исходный список:',lst)

new_lst = [lst[el] for el in range(len(lst)) if lst[el]>lst[el-1] and el !=0]

print('Сортированный список:',new_lst)

