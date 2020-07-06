print ("Hello World!!")
if 1 > 0:
    print("1 は 0 より大きい")
def add(x,y):
    num = x + y
    return num
# コメントはソースコードを読んでも処理が不明確な場合のみ書く

# 定数
print(100)
# 変数
z = 1
print(z)
z = 2
print(z)
# 2つ以上の単語はスネークケースでつなげる
user_id = "admin"
selling_price = 2500
print(user_id)


# 課題1
def sum(x,y):
    return x + y


def difference(x,y):
    return x - y


def product(x,y):
    return x * y


def quotient(x,y):
    return x // y


def surplus(x,y):
    return x % y

x = 11
y = 3

sum = sum(x,y)
print("11 + 3 = " + str(sum))

difference = difference(x,y)
print("11 - 3 = " + str(difference))

product = product(x,y)
print("11 × 3 = " + str(product))

quotient = quotient(x,y)
surplus = surplus(x,y)
print("11 ÷ 3 = " + str(quotient) + " 余り " + str(surplus))

# 課題2  
print("1つ目の値を入力してください")
num1 = int(input())
print("2つ目の値を入力してください")
num2 = int(input())

total = sum(num1 + num2)


