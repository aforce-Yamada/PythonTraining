import datetime
from dateutil.relativedelta import relativedelta
from python2_test2_2 import is_leap_year

#100で割り切れて400で割り切れない
def test_is_leap_year_01():
    value = is_leap_year(2100)
    assert value == False


#4で割り切れる
def test_is_leap_year_02():
    value = is_leap_year(2000)
    assert value == True


#どちらにも当てはまらない
def test_is_leap_year_03():
    value = is_leap_year(2001)
    assert value == False