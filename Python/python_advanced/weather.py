# 날씨 정보 받아오기
# https://openweathermap.org/current

import requests
import json

city = "Seoul"
apikey = "f406a6b7eaf954f751eb0deb7c355ba6" ################################ 보안 문제로 #으로 설정
lang = "kr"

api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"


result = requests.get(api)
data = json.loads(result.text)

city_name = data["name"]
print(f"{city_name}의 날씨입니다.")
print("날씨는",data["weather"][0]["description"],"입니다.")
print("현재 온도는",data["main"]["temp"],"입니다.")
print("하지만 체감 온도는",data["main"]["feels_like"],"입니다.")
print("최저 기온은",data["main"]["temp_min"],"입니다.")
print("최고 기온은",data["main"]["temp_max"],"입니다.")
print("습도는",data["main"]["humidity"],"입니다.")
print("기압은",data["main"]["pressure"],"입니다.")
print("풍향은",data["wind"]["deg"],"입니다.")
print("풍속은",data["wind"]["speed"],"입니다.")