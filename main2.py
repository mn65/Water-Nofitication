from plyer import notification 
import time

while True:
    notification.notify(
        title = "**Please Drink water..",
        message = '''Water is your body's principal chemical component and makes up about 50% to 70% of your body weight. 
        Your body depends on water to survive.''',
        app_icon = "D:\water notfication code python\icon.ico",
        timeout = 10

    )
    time.sleep(60*60)