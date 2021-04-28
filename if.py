
num1 = input("1번 수: ")
num2 = input("2번 수: ")

print(type(num1))
print(type(num2))

print("num1 + num2 = ", int(num1) + int(num2))
print("당신이 입력한 수: " , num1, num2)
print("당신이 입력한 수: {0}, {1}".format(num1, num2))
print("당신이 입력한 수: %s, %s" % (num1, num2))

if num1 > num2:
    print("num1이 크다")
elif num1 < num2:
    print("num2이 크다")
else:
    print("두수는 같다")