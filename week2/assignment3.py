def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
    def Mergesort(nums):
        if len(nums) > 1:
            middle = len(nums)//2
            l = nums[:middle]
            r = nums[middle:]
            Mergesort(l)
            Mergesort(r)

            i = 0
            j = 0
            k = 0

            while i < len(l) and j < len(r):
                if l[i] <= r[j]:
              # The value from the left half has been used
                    nums[k] = l[i]
              # Move the iterator forward
                    i += 1
                else:
                    nums[k] = r[j]
                    j += 1
            # Move to the next slot
                k += 1

            while i < len(l):
                nums[k] = l[i]
                i += 1
                k += 1
            while j < len(r):
                nums[k]=r[j]
                j += 1
                k += 1

    if len(nums) == 1:
        print(nums)
        return nums
    else:
        Mergesort(nums)
        if (nums[-1]*nums[-2]) >= (nums[0]*nums[1]):
            print(nums[-1]*nums[-2])
        elif (nums[-1]*nums[-2]) <= (nums[0]*nums[1]):
            print(nums[0]*nums[1])

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2