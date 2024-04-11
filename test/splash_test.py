import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

# 如果lua代码中有特殊字符，要通过进行quote转码
from urllib.parse import quote


if __name__ == '__main__':
    url = 'https://sso.ecust.edu.cn/authserver/login?service=http://s.ecust.edu.cn/sso/ecustsb'
    with open("main.lua", "r") as f:
        lua = f.read()
    base_url = f'http://localhost:8050/execute?url={url}&lua_source={quote(lua)}'
    response = requests.get(base_url)
    if response.status_code == 200:
        # 从二进制数据中创建图像
        img = Image.open(BytesIO(response.content))
        # 显示图像
        plt.imshow(img)
        plt.show()
    else:
        print("截图请求失败", response.text)
