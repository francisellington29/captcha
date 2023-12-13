from datetime import datetime

import pytz

timezone = pytz.timezone('Asia/Shanghai')

def current_time():
    current_time = datetime.now(timezone)
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time