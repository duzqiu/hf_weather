import flet as ft

def main(page: ft.Page):
    page.title = "Flet Icons 示例"
    page.padding = 20
    page.scroll = "adaptive"

    # 示例1：使用 ft.Icon（推荐方式）
    icon1 = ft.Icon(
        name=ft.Icons.CHECK_CIRCLE,  # ✅ 勾选圆圈
        color="green",
        size=40
    )

    # 示例2：天气图标（类似 QWeather 的 sunny）
    icon2 = ft.Icon(
        name=ft.Icons.WB_SUNNY,      # 🌤 晴天
        color="orange",
        size=40
    )

    # 示例3：爱心
    icon3 = ft.Icon(
        name=ft.Icons.FAVORITE,      # ❤️ 爱心
        color="red",
        size=40
    )

    # 示例4：主页
    icon4 = ft.Icon(
        name=ft.Icons.HOME,          # 🏠 主页
        color="blue",
        size=40
    )

    # 示例5：添加按钮图标
    icon5 = ft.Icon(
        name=ft.Icons.SUNNY,    # ➕ 圆圈加号
        color="green",
        size=40
    )

    # 将图标放入按钮中
    button = ft.ElevatedButton(
        text="点击我",
        icon=ft.Icons.WB_CLOUDY,     # 👍 拇指向上
        on_click=lambda e: print("点赞！")
    )

    # 浮动按钮也支持图标
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.PLAY_ARROW,   # ▶ 播放按钮
        bgcolor="pink",
        on_click=lambda e: print("播放！")
    )

    # 页面内容
    page.add(
        ft.Column(
            [
                ft.Text("Flet 内置 Icons 示例", size=24, weight="bold"),
                ft.Divider(),

                ft.Row([ft.Text("✅:", size=16), icon1]),
                ft.Row([ft.Text("🌤:", size=16), icon2]),
                ft.Row([ft.Text("❤️:", size=16), icon3]),
                ft.Row([ft.Text("🏠:", size=16), icon4]),
                ft.Row([ft.Text("➕:", size=16), icon5]),

                ft.Divider(),
                button,
            ],
            
            spacing=15,
            alignment="start"
        )
    )

# 运行应用（无需 assets_dir）
ft.app(target=main)