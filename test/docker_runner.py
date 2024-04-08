import docker

global process

# 连接 Docker 守护程序
client = docker.from_env()

# 启动一个容器
container = client.containers.run("scrapinghub/splash", detach=True, ports={'8050': 8050})

if __name__ == '__main__':
    input()
    container.stop()
