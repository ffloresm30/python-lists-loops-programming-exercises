sample_list = [45, 67, 87, 23, 5, 32, 60]
 

# Your code below
print ( "initial list : " , sample_list)
new_list = []
for i in (range(len(sample_list)-1, -1, -1)):
    new_list.append(sample_list[i])
    
print( "final list: " , new_list)
