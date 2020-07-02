debt = 250000
interest = (0.14 / 12)
repayment = 30000
n = 0

while debt > repayment:
        debt = debt + (debt * interest) - repayment
        n += 1

        print(str(n) + "ヶ月目：返済額=" + str(repayment) + "円, 残り" + str(debt) + "円")

debt = debt + (debt * interest)
n += 1
print(str(n) + "ヶ月目：返済額=" + str(debt) + "円, 返済完了")