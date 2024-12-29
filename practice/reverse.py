def reverse(nums):
  right = len(nums) - 1
  left = 0
  while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    right = right-1
    left = left +1
  return nums
        
print(reverse([1,2,3,4,5,6,7]))
