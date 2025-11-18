#!/usr/bin/env python3
from lib.MySet import MySet

# Create a new empty set
empty_set = MySet()
print(f"Empty set: {empty_set}")

# Create a set with initial values (duplicates removed)
set_with_values = MySet([1, 2, 3, 3, 4, 4])
print(f"Set with values: {set_with_values}")

# Add a value
set_with_values.add(5)
print(f"After adding 5: {set_with_values}")

# Check if value exists
print(f"Has 3? {set_with_values.has(3)}")
print(f"Has 10? {set_with_values.has(10)}")

# Get size
print(f"Size: {set_with_values.size()}")

# Delete a value
set_with_values.delete(2)
print(f"After deleting 2: {set_with_values}")

# Clear the set
set_with_values.clear()
print(f"After clear: {set_with_values}")

# Example: Finding first repeated value
def first_repeated_value(list):
    # Create a Set to keep track of values we've seen
    number_set = MySet()
    # Iterate over each element from the list
    for i in range(0, len(list)):
        # If we've already seen a value, we've found the duplicate!
        if number_set.has(list[i]):
            return list[i]
        # Otherwise, add the value to our set
        number_set.add(list[i])
    # Return None if we reach the end and haven't found our value
    return None

print(f"\nFirst repeated value in [1,2,3,3,4,4]: {first_repeated_value([1,2,3,3,4,4])}")
