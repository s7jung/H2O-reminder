import time
from plyer import notification
import popup
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Please Drink A Cup Of Water Now!!",
            message ="Drinking Water Helps to Maintain the Balance of Body Fluids.",
            app_icon='water.png',
            timeout= 10
            )
        time.sleep(60*60*time_interval)