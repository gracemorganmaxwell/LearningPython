# Define a set of cat weights
cat_weights = {8, 10, 6, 12, 7}

# Check if a given value is present in the set
value_to_check = 10
is_present = value_to_check in cat_weights

# Display the results
print("Cat Weights Set:", cat_weights)
print(f"Is {value_to_check} present in the set?:", is_present)

'''
Output will be:
Cat Weights Set: {6, 7, 8, 10, 12}
Is 10 present in the set?: True

In this set of cat weights, checking for the value 10 returns True, indicating that there is at least one cat in the 
set that weighs 10 pounds

'''