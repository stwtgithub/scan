from config import default


class Settings(object):
    def __init__(self):
        # 获取全局变量中的配置信息
        for attr in dir(default):
            setattr(self, attr, getattr(default, attr))


settings = Settings()