nums = [34,45,23,68,26,99,56]
i = 0
work = 0
highest = nums[0]
while i < len(nums):
    work = work + 1
    if nums[i] > highest:
        highest = nums[i]
    i = i + 1
print("Highest number is: ", highest)
print("The algorithm used ", work, " units of work")

