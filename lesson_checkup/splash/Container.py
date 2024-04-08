import docker

from . import container_name, port


def singleton(cls):
    """
    This is a decorator that can be used to create a singleton out of a class.
    """
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Container:
    """
    This class represents a Docker container.
    It is a singleton that can be used to interact with a Docker container.
    The container is created when the class is instantiated.
    """

    def __init__(self):
        self.__exist = False
        print("Attempting to create Docker client...")
        self._client = docker.from_env()
        print("Docker client created successfully.")
        try:
            self._container = self._client.containers.get(container_name)
            self.__exist = True
        except docker.errors.NotFound:
            print("Container does not exist. ")

    def refresh(self):
        try:
            self._container = self._client.containers.get(container_name)
            self.__exist = True
        except docker.errors.NotFound:
            print("Container does not exist. ")
            self.__exist = False

    def run(self):
        if not self.__exist:
            print("Attempting to pull the image...")
            self._container = self._client.containers.run("scrapinghub/splash", name=container_name, detach=True,
                                                          ports={'8050': port})
            print("Image pulled successfully.")
            print("Container start successfully.")
        else:
            if self._container.status == "exited":
                self._container.restart()
                print("Container restart successfully.")
            else:
                print("Container is already running.")
        self.refresh()

    def stop(self):
        if not self.__exist:
            raise Exception("Container does not exist. ")
        if self._container.status == "running":
            self._container.stop()
            print("Container stop successfully.")
        else:
            print("Container is already stopped.")
        self.refresh()

    def __del__(self):
        if self.__exist and self._container.status == "running":
            self._container.stop()
