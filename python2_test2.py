import datetime
from dateutil.relativedelta import relativedelta


def leap_year(year):
    if year % 100  == 0 and year % 400 != 0:
        #print(str(year) + "年は平年です")
        return False
    elif year % 4 == 0:
        #print(str(year) + "年は閏年です")
        return True
    else:
        #print(str(year) + "年は平年です")
        return False


today = datetime.date.today()
one_year_ago = (today + relativedelta(years=-1))
one_year_later = (today + relativedelta(years=1))
years = [today.year, one_year_ago.year, one_year_later.year]

for year in years:
    leap_check = leap_year(year)
    if leap_check == True:
        print(str(year) + "年は閏年です")
    else:
        print(str(year) + "年は平年です")