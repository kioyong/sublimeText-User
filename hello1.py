import sys
import os
# import Image
from PIL import Image, ImageDraw
h,s,v,r,g,b = 226.15384615384608,0.06074766355140192,0.8392156862745098,140,142,149
def pull_screenshot():
    process = subprocess.Popen('adb shell screencap -p', shell=True, stdout=subprocess.PIPE)
    screenshot = process.stdout.read().replace(b'\r\n', b'\n')
    f = open('C:/Users/LiangYong/workspace/wechat_jump_game/autojump.png', 'wb')
    f.write(screenshot)
    f.close()

# print(h, s, v)
# print(r, g, b)
# print(sys.platform)
# print(sys.version)
# process = subprocess.Popen('adb shell screencap -p', shell=True, stdout=subprocess.PIPE)
# screenshot = process.stdout.read()
# binary_screenshot = screenshot.replace(b'\r\n', b'\n')
# print("binary_screenshot = ",binary_screenshot)
# print(os.path.isfile('C:/Users/LiangYong/workspace/wechat_jump_game/autojump.png'))
print("start")
# pull_screenshot()
# im = Image.open('./autojump.png')
# print("end")