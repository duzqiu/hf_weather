# 天气相关api配置

class WeatherConfig:
    # 和风天气KEY
    KEY = "aedc97eaa1fd4b148476a0afa47c60ee"
    # 根据地名 IP 经纬获取城市ID的URL地址
    LOCATION = "https://geoapi.qweather.com/v2/city/lookup"
    # 实时天气查询URL地址
    WEATHER_NOW = "https://devapi.qweather.com/v7/weather/now"



weather_config = WeatherConfig()


