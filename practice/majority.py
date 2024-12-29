def majorityElement(nums):
        m = 0
        count = 0
        for num in nums:
          if count == 0 and num != m:
            m = num
            count =+ 1
          elif m == num:
            count = count + 1
            print("yyy", count)
          else:
            count -= 1
          print(m)
          print(count)
        return m
        

print(majorityElement([6,6,6,7,7]))
