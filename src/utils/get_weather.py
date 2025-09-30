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
        self.location_warning_url = weather_config.LOCATION_WARNING
        self.weather_now_url = weather_config.WEATHER_NOW
        self.warning = weather_config.WARNING

    def get_location_id(self, loc): # 中国城市代码查询
        location_url = self.location_url
        params = {"location": loc,"key": self.key}
        location_resp = requests.get(location_url, params=params)
        location_id = location_resp.json()['location'][0]['id']
        return location_id

    def get_location_warning_id(self, city): # 天气预警城市列表
        location_url = self.location_warning_url
        params = {"range": city,"key": self.key}
        location_resp = requests.get(location_url, params=params)
        location_id = location_resp.json()['warningLocList']
        return location_id
    
    def get_weather_now(self, loc_id): # 实时天气查询
        weather_url = self.weather_now_url
        params = {"location": loc_id,"key": self.key}
        weather_resp = requests.get(weather_url,params=params)
        weather_list = weather_resp.json()['now']
        return weather_list

        # obs_time = weather_list['obsTime'] # 观测时间
        # update_time = weather_resp.json()['updateTime'] # 更新时间

        # temp = weather_list['temp']  # 温度
        # feels_like = weather_list['feelsLike']  # 体感温度
        # dew = weather_list['dew'] # 露点温度

        # text = weather_list['text']  # 天气
        # icon = weather_list['icon'] # 天气图标代码

        # wind_dir = weather_list['windDir']  # 风向
        # wind_scale = weather_list['windScale']  # 风力等级
        # wind360 = weather_list['wind360'] # 风向360角度
        # wind_speed = weather_list['windSpeed'] # 风速

        # humidity = weather_list['humidity'] # 湿度
        # precip = weather_list['precip'] # 降水量
        # pressure = weather_list['pressure'] # 大气压强

        # vis = weather_list['vis'] # 能见度
        # cloud = weather_list['cloud'] # 云量
        
        # return obs_time,update_time,text,icon,temp,feels_like,wind_dir,wind_scale,wind360,wind_speed,humidity,precip,pressure,vis,cloud,dew
    
    def get_weather_day(self, loc_id, day): # 逐日天气预报
        weather_3d_url = f"{weather_config.WEATHER}/{day}"
        params = {"location": loc_id,"key": self.key}
        weather_3d_resp = requests.get(weather_3d_url, params=params)
        daily_list = weather_3d_resp.json()['daily']
        return daily_list
    
    def get_weather_hour(self, loc_id, hour): # 逐小时天气预报
        weather_hour_url = f"{weather_config.WEATHER}/{hour}"
        params = {"location": loc_id,"key": self.key}
        weather_hour_resp = requests.get(weather_hour_url, params=params)
        hourly_list = weather_hour_resp.json()['hourly']
        return hourly_list
    
    def get_weather_warning(self, lang, loc): #天气灾害预警
        weather_warning_url = weather_config.WARNING
        params = {"location": loc, "lang": lang,"key": self.key}
        weather_warning_resp = requests.get(weather_warning_url, params=params)
        warning_list = weather_warning_resp.json()['warning']
        return warning_list

    def get_weather_indices(self, loc_id, type, day): # 天气指数信息
        weather_indices_url = f"{weather_config.INDICES}/{day}"
        params = {"location": loc_id, "type": type,"key": self.key}
        weather_indices_resp = requests.get(weather_indices_url, params=params)
        indices_list = weather_indices_resp.json()['daily']
        return indices_list

if __name__ == "__main__":
    weather = Weather()
    loc_id = weather.get_location_id("浦东新区")
    print(loc_id)
    weather_info = weather.get_weather_indices(loc_id,"1,2,3","1d")
    print(weather_info)