import requests
from PIL import Image
from io import BytesIO


if __name__ == '__main__':
    url = 'https://www.google.com.hk/'
    payload = {
        'url': url,
        'render_all': True,  # 渲染整个页面
        'width': 1280,  # 截图宽度
        'height': 800,  # 截图高度
        'timeout': 30,  # 页面加载超时时间
        'viewport': '1280x800',  # 视口大小
        'format': 'png',  # 截图格式
    }

    response = requests.post('http://127.0.0.1:8050/render.png', json=payload)
    if response.status_code == 200:
        # 从二进制数据中创建图像
        img = Image.open(BytesIO(response.content))
        # 显示图像
        img.show()
    else:
        print("截图请求失败，状态码：", response.status_code)