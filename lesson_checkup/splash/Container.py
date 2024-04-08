import docker


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Container:
    def __init__(self):
        self._client = docker.from_env()
        self._container = None

    def run(self):
        # 启动一个容器
        self._container = self._client.containers.run("scrapinghub/splash", detach=True, ports={'8050': 8050})

    def stop(self):
        # 停止容器
        self._container.stop()
