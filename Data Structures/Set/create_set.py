"""
Sets in Python are a type of data structure that allows you to store multiple items in a single variable. They are
dynamic, meaning you can add or remove items after the set has been created. Sets are implemented as hash tables,
which provide very efficient lookup times, making them ideal for checking membership—that is, testing whether an item
is present in the set.

What is a Set?
A set is a collection that is both unordered and unindexed. In Python, sets are written with curly
brackets, and they can contain elements of different immutable data types.

Key Characteristics of Sets in Python:

Uniqueness:
The defining feature of a set is that it only holds unique elements. If you try to add a duplicate item
to a set, Python will simply ignore the addition, maintaining just one instance of every element.

Unordered:
Sets do not maintain any order for stored items, which means the items do not have a fixed position; you
cannot refer to them by an index or key as you would with lists or dictionaries.

Mutability:
While sets themselves can be modified by adding or removing items, the individual elements within a set
must be of immutable types (such as integers, floats, strings, and tuples). This immutability is required because
behind the scenes, the set uses these immutable objects as keys in a hash table.

Efficient Membership Testing:
Sets are optimized for determining whether a specific element is present. This
operation, called a membership test, is much faster in a set than in a list or tuple because sets use a hash function
to map each item to a unique position, which allows for quick lookups.

Using Sets as a Data Structure:
Sets are often used in scenarios where the presence or uniqueness of items is more
important than their order or their position within a collection.

Common use cases for sets include:
Removing duplicates from a collection. Performing mathematical set operations like
unions, intersections, and set differences. Quickly checking for the presence of an element without having to search
through the entire data structure.

How Sets Work in Python:
When you add items to a set, Python uses a hash function to determine where in
the set's underlying hash table the item should be placed. This hashing mechanism is what makes sets so efficient for
membership tests and why sets require their elements to be immutable (and thus hashable).

"""

# Creating a set of cat breeds
cat_breeds = {"Tabby", "Siamese", "Persian"}
print("Initial Cat Breeds:", cat_breeds)

# Adding a cat breed to the set
cat_breeds.add("Maine Coon")
print("After Adding Maine Coon:", cat_breeds)

# Adding multiple cat breeds to the set at once
cat_breeds.update(["Bengal", "Sphynx", "Ragdoll"])
print("After Adding Multiple Breeds:", cat_breeds)

# Trying to add a duplicate breed to the set
cat_breeds.add("Siamese")  # This will have no effect because "Siamese" is already in the set
print("After Trying to Add Duplicate Siamese:", cat_breeds)

# Removing a cat breed from the set
cat_breeds.remove("Tabby")
print("After Removing Tabby:", cat_breeds)

# Membership test to check if a breed is in the set
print("Is Siamese in the set?", "Siamese" in cat_breeds)
print("Is Burmese in the set?", "Burmese" in cat_breeds)

# Set operations with another set of cat breeds
exotic_cat_breeds = {"Sphynx", "Bengal", "Savannah"}
print("Union of Breeds:", cat_breeds.union(exotic_cat_breeds))
print("Intersection of Breeds:", cat_breeds.intersection(exotic_cat_breeds))
print("Difference of Breeds:", cat_breeds.difference(exotic_cat_breeds))


"""
From our example above:

> A set named cat_breeds is created containing some cat breeds.
> A new breed is added using the add method.
> Multiple new breeds are added using the update method.
> An attempt is made to add a duplicate breed, which has no effect because sets do not allow duplicates.
> A breed is removed using the remove method.
> Membership tests are performed to check if certain breeds are present in the set.
> Set operations like union, intersection, and difference are demonstrated with another set named exotic_cat_breeds.
"""