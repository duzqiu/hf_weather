# 天气相关api配置

class WeatherConfig:
    API_HOST = "https://kq6appj269.re.qweatherapi.com"
    # 和风天气KEY
    KEY = "aedc97eaa1fd4b148476a0afa47c60ee"
    # 根据地名 IP 经纬获取城市ID的URL地址
    LOCATION = "https://geoapi.qweather.com/v2/city/lookup"
    # 预警城市查询ID
    LOCATION_WARNING = f"{API_HOST}/v7/warning/list"
    # 实时天气查询URL地址
    WEATHER_NOW = "https://devapi.qweather.com/v7/weather/now"
    # 逐日天气预报URL地址
    # 3d 3天预报。
    # 7d 7天预报。
    # 10d 10天预报。
    # 15d 15天预报。
    # 30d 30天预报。

    # 24h 24小时预报。
    # 72h 72小时预报。
    # 168h 168小时预报。
    WEATHER = "https://devapi.qweather.com/v7/weather"
    #天气灾害预警
    WARNING = f"{API_HOST}/v7/warning/now"
    
    # 天气指数类型	API类型值	iOS Indices	Android Indices
    # 全部天气指数	0	ALL	ALL
    # 运动指数	1	SPT	SPT
    # 洗车指数	2	CW	CW
    # 穿衣指数	3	DRSG	DRSG
    # 钓鱼指数	4	FIS	FIS
    # 紫外线指数	5	UV	UV
    # 旅游指数	6	TRA	TRA
    # 花粉过敏指数	7	AG	AG
    # 舒适度指数	8	COMF	COMF
    # 感冒指数	9	FLU	FLU
    # 空气污染扩散条件指数	10	AP	AP
    # 空调开启指数	11	AC	AC
    # 太阳镜指数	12	GL	GL
    # 化妆指数	13	MU	MU
    # 晾晒指数	14	DC	DC
    # 交通指数	15	PTFC	PTFC
    # 防晒指数	16	SPI	SPI
    # 天气指数信息
    INDICES = f"{API_HOST}/v7/indices"
    



weather_config = WeatherConfig()


