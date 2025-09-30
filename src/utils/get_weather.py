import sys
import os

# 将项目根目录添加到模块搜索路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import requests
from src.config.config import weather_config


class Weather:
    def __init__(self):
        self.key = weather_config.KEY
        self.location_url = weather_config.LOCATION
        self.weather_now_url = weather_config.WEATHER_NOW

    def get_location_id(self, loc):
        # 中国城市代码查询
        location_url = f"{self.location_url}?location={loc}&key={self.key}"

        location_resp = requests.get(location_url)
        location_id = location_resp.json()['location'][0]['id']
        return location_id

    def get_weather(self, loc_id):
        # 实时天气查询
        weather_url = f"{self.weather_now_url}?location={loc_id}&key={self.key}"
        weather_resp = requests.get(weather_url)
        # print(weather_resp.json())
        obs_time = weather_resp.json()['now']['obsTime'] # 观测时间

        update_time = weather_resp.json()['updateTime'] # 更新时间
        temp = weather_resp.json()['now']['temp']  # 温度
        feels_like = weather_resp.json()['now']['feelsLike']  # 体感温度
        text = weather_resp.json()['now']['text']  # 天气
        wind_dir = weather_resp.json()['now']['windDir']  # 风向
        wind_scale = weather_resp.json()['now']['windScale']  # 风力等级

        wind360 = weather_resp.json()['now']['wind360'] # 风向360角度
        wind_speed = weather_resp.json()['now']['windSpeed'] # 风速
        humidity = weather_resp.json()['now']['humidity'] # 湿度
        precip = weather_resp.json()['now']['precip'] # 降水量
        pressure = weather_resp.json()['now']['pressure'] # 大气压强
        vis = weather_resp.json()['now']['vis'] # 能见度
        cloud = weather_resp.json()['now']['cloud'] # 云量
        dew = weather_resp.json()['now']['dew'] # 露点温度
        return update_time,text,temp,feels_like,wind_dir,wind_scale,wind360,wind_speed,humidity,precip,pressure,vis,cloud,dew
    
if __name__ == "__main__":
    weather = Weather()
    loc_id = weather.get_location_id("北京")
    print(loc_id)
    weather_info = weather.get_weather(loc_id)
    print(weather_info)