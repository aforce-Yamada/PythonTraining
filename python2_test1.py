print("速度(km/h)を入力してください")
speed = int(input())
print("距離(km)を入力してください")
distance = int(input())

def time(distance,speed):
    result = distance / speed
    return result


time = time(distance,speed)
print(str(time * 60) + "分")