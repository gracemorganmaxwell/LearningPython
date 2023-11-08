# Define two sets of cat breeds
set1 = {"Siamese", "Persian", "Maine Coon"}
set2 = {"Bengal", "Ragdoll", "Maine Coon"}

# Perform the union operation
union_of_sets = set1.union(set2)

# Display the results
print("Set 1:", set1)
print("Set 2:", set2)
print("Union of Set 1 and Set 2:", union_of_sets)

'''
The output: 

Set 1: {'Persian', 'Siamese', 'Maine Coon'}
Set 2: {'Maine Coon', 'Ragdoll', 'Bengal'}
Union of Set 1 and Set 2: {'Siamese', 'Maine Coon', 'Persian', 'Ragdoll', 'Bengal'}

The union of set1 and set2 results in a new set that contains all unique elements from both set1 and set2. Since 
"Maine Coon" is present in both sets, it appears only once in the union, as sets do not allow duplicate elements.

'''