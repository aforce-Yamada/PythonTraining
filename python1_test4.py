debt = 250000
interest = (0.14 / 12)
repayment = 30000
month = 0

while debt > 0:
    month += 1
    debt = debt + (debt * interest)

    if debt > repayment:
        debt -= repayment
        print(str(month) + "ヶ月目：返済額=" + str(repayment) + "円, 残り" + str(debt) + "円")
    else:
        repayment = debt
        debt = 0
        print(str(month) + "ヶ月目：返済額=" + str(repayment) + "円, 返済完了")
