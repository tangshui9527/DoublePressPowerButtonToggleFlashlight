import struct
import time
import os
import subprocess
import threading

# 定义事件文件的路径和事件代码
EVENT_FILE = '/dev/input/event0'
# 你的电源键代码，从你提供的getevent输出中确定
KEY_SEARCH_CODE = 0x74  
KEY_PRESS_VALUE = 0x01

# 定义双击的时间间隔（毫秒）
DOUBLE_CLICK_INTERVAL_MS = 500

# 全局变量来追踪闪光灯状态，默认为关闭
flashlight_on = False

# 用于记录上一次按键时间
last_press_time = 0

def toggle_flashlight_with_am():
    """
    使用 am start 和 am force-stop 命令来切换闪光灯状态。
    这个方法依赖于 com.meizu.flyme.toolbox 这个应用的行为。
    """
    global flashlight_on
    
    # 打印当前状态，方便调试
    print(f"Current flashlight status before toggle: {'ON' if flashlight_on else 'OFF'}")
    
    try:
        if not flashlight_on:
            print("Attempting to turn flashlight ON by starting FlashLightActivity...")
            # 启动魅族工具箱的闪光灯Activity
            os.system('am start -n com.meizu.flyme.toolbox/.activity.FlashLightActivity')
            flashlight_on = True
        else:
            print("Attempting to turn flashlight OFF by force stopping the app...")
            # 强制停止魅族工具箱，以关闭闪光灯
            os.system('am force-stop com.meizu.flyme.toolbox')
            flashlight_on = False
        
        print(f"Flashlight state after toggle: {'ON' if flashlight_on else 'OFF'}")
        
    except Exception as e:
        print(f"Failed to toggle flashlight: {e}")

def main():
    global last_press_time

    # 事件的格式，每个事件由24字节组成
    event_format = 'llHHI'
    event_size = struct.calcsize(event_format)

    try:
        # 以二进制模式打开事件文件
        with open(EVENT_FILE, 'rb') as f:
            print(f"Monitoring {EVENT_FILE} for double-click...")

            while True:
                data = f.read(event_size)
                # 解析事件数据
                _, _, event_type, code, value = struct.unpack(event_format, data)

                # 检查是否为按键按下事件和正确的按键代码
                if event_type == 1 and code == KEY_SEARCH_CODE and value == KEY_PRESS_VALUE:
                    current_time_ms = int(time.time() * 1000)

                    # 判断是否为双击
                    if current_time_ms - last_press_time < DOUBLE_CLICK_INTERVAL_MS:
                        print("Double-click detected!")
                        # 启动一个新线程来执行切换操作，避免阻塞事件监听
                        threading.Thread(target=toggle_flashlight_with_am).start()
                        last_press_time = 0  # 重置，避免三次点击
                    else:
                        last_press_time = current_time_ms
    
    except FileNotFoundError:
        print(f"Error: {EVENT_FILE} not found. Are you sure you have root access and the file exists?")
    except PermissionError:
        print("Error: Permission denied. Make sure you are running with root and file permissions are correct.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
