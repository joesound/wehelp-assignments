def maxZeros(nums):
# 請用你的程式補完這個函式的區塊
    dummy = 0
    current = 0
    for i in nums:
        if i == 0:
            dummy +=1
        else:
            if current >= dummy:
                dummy = 0
            else:
                current = dummy
                dummy = 0
    print(current)
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3