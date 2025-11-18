#!/usr/bin/env python3
from lib.MySet import MySet

empty_set = MySet()
print(f"Empty set: {empty_set}")

set_with_values = MySet([1, 2, 3, 3, 4, 4])
print(f"Set with values: {set_with_values}")

set_with_values.add(5)
print(f"After adding 5: {set_with_values}")

print(f"Has 3? {set_with_values.has(3)}")
print(f"Has 10? {set_with_values.has(10)}")

print(f"Size: {set_with_values.size()}")

set_with_values.delete(2)
print(f"After deleting 2: {set_with_values}")

set_with_values.clear()
print(f"After clear: {set_with_values}")

def first_repeated_value(list):
    number_set = MySet()
    for i in range(0, len(list)):
        if number_set.has(list[i]):
            return list[i]
        number_set.add(list[i])
    return None

print(f"\nFirst repeated value in [1,2,3,3,4,4]: {first_repeated_value([1,2,3,3,4,4])}")
