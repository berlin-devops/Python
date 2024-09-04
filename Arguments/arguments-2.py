def add(x, y):
    return x + y

nums = [2, 4]

print(f'Example1')
print(f'add(*nums):\n{add(*nums)}') # 6
print(f'\n')

print(f'Example2')
# Example 2
nums2 = {"x": 15, "y": 25}
print(f'add(nums2["x"], nums["y"]):\n{add(nums2["x"], nums2["y"])}') # 40
print(f'\n')
# Another way
print(f'Another way of expression')
print(f'add(x=nums2["x"], y=nums["y"]):\n{add(x=nums2["x"], y=nums2["y"])}')
