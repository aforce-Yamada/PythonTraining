print("身長(m)を入力してください")
height = float(input())
print("体重(kg)を入力してください")
weight = float(input())

bmi = weight / height ** 2
print(bmi)

message = "message"

if bmi < 18.5:
    message = "やせ"
elif 18.5 <= bmi < 25:
    message = "標準"
elif 25 <= bmi < 30:
    message = "肥満"
else:
    message = "高度肥満"

print("＜実行結果＞")
print("あなたは「" + str(message) + "」です。")
