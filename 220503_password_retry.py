password = 'a123456'
x = 3
print('密碼重試程式練習')

while x <= 3 and x > 0:
    print('請輸入密碼！')
    input_password = input('密碼：')
    if input_password == password:
        print('登入成功')
        break
    elif x >= 1:
        x = x - 1
        print('密碼錯誤，還有',x,'次機會')
else:
    print('登入失敗！')