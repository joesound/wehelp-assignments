def calculate(min, max):
# 請用你的程式補完這個函式的區塊
    dummy  = 0
    for i in range(min,max+1):
        dummy = dummy + i
    print(dummy)
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30