# Define two sets of cat breeds
set1 = {"Siamese", "Persian", "Maine Coon"}
set2 = {"Bengal", "Ragdoll", "Maine Coon"}

# Perform set difference operations
difference_set1 = set1.difference(set2)  # Elements in set1 but not in set2
difference_set2 = set2.difference(set1)  # Elements in set2 but not in set1

# Display the results
print("Set 1:", set1)
print("Set 2:", set2)
print("Set Difference (Set 1 - Set 2):", difference_set1)
print("Set Difference (Set 2 - Set 1):", difference_set2)

'''
Output: 

Set 1: {'Persian', 'Siamese', 'Maine Coon'}
Set 2: {'Maine Coon', 'Ragdoll', 'Bengal'}
Set Difference (Set 1 - Set 2): {'Persian', 'Siamese'}
Set Difference (Set 2 - Set 1): {'Ragdoll', 'Bengal'}

The set difference operation yields two sets:

> The first set contains breeds found in set1 but not in set2, which are 'Persian' and 'Siamese'.
> The second set contains breeds found in set2 but not in set1, which are 'Ragdoll' and 'Bengal'.
'''